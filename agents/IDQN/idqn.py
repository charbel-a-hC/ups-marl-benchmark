import numpy as np
import torch
import torch.nn as nn

from pfrl import explorers, replay_buffers
from pfrl.agents import DQN
from pfrl.q_functions import DiscreteActionValueHead

from agents.agent import Agent, IndependentAgent


class DQNAgent(Agent):
    def __init__(self, config, act_space, model):
        super().__init__()

        self.model = model
        self.optimizer = torch.optim.Adam(self.model.parameters())
        replay_buffer = replay_buffers.ReplayBuffer(10000)


        explorer = explorers.LinearDecayEpsilonGreedy(
            config['EPS_START'],
            config['EPS_END'],
            config['steps'],
            lambda: np.random.randint(act_space),
        )

        self.agent = DQN(self.model, self.optimizer, replay_buffer, config['GAMMA'], explorer,
                         
                         minibatch_size=config['BATCH_SIZE'], replay_start_size=config['BATCH_SIZE'],
                         phi=lambda x: np.asarray(x, dtype=np.float32),
                         target_update_interval=config['TARGET_UPDATE'])

    def act(self, observation):
        return self.agent.act(observation)

    def observe(self, observation, reward, done, info):
        self.agent.observe(observation, reward, done, False)

    def save(self, path):
        torch.save({
            'model_state_dict': self.model.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict(),
        }, path+'.pt')
        
    def get_statistics(self):
        return self.agent.get_statistics()

class IDQN(IndependentAgent):
    def __init__(self, config, obs_act):
        super().__init__(config, obs_act)
        for key in obs_act:
            obs_space = obs_act[key][0]
            act_space = obs_act[key][1]

            def conv2d_size_out(size, kernel_size=2, stride=1):
                return (size - (kernel_size - 1) - 1) // stride + 1

            h = conv2d_size_out(obs_space[1])
            w = conv2d_size_out(obs_space[2])

            model = nn.Sequential(
                nn.Conv2d(obs_space[0], 64, kernel_size=(2, 2)),
                nn.ReLU(),
                nn.Flatten(),
                nn.Linear(h * w * 64, 64),
                nn.ReLU(),
                nn.Linear(64, 64),
                nn.ReLU(),
                nn.Linear(64, act_space),
                DiscreteActionValueHead()
            )

            self.agents[key] = DQNAgent(config, act_space, model)
    
    def get_statistics(self):
        for agent in self.agents:
            print(self.agents[agent].get_statistics())