from ast import parse
import gym
import highway_env
import argparse

import numpy as np
from tqdm import trange

from env_config import ENV_CONFIG

def populate_parser(parser: argparse.ArgumentParser):
    
    parser.add_argument(
        "--train",
        "-t",
        dest= "train",
        type= bool,
        default= True,
        help= "Training or Testing, if testing is desired, a trained model path should be given"
    )
    parser.add_argument(
        "--model_path",
        dest= "model_path",
        type= str,
        help= "Trained model path"
    )
    parser.add_argument(
        "--env",
        "-e",
        dest= "env",
        type= str,
        help= "Type of environment from highway-env",
        default= "highway-v0",
        choices= [
            "highway-v0",
            "highway-fast-v0",
            "merge-v0",
            "roundabout-v0",
            "intersection-v0",
            "racetrack-v0"
        ],   
    )
    parser.add_argument(
        "--agent",
        "-a",
        dest= "agent",
        type= str,
        default= "IDQN",
        choices= [
            "IDQN", "IPPO"
        ]
    )

def main(args):
    EPISODES = 1000
    
    agent = args.agent
    env = gym.make(args.env)
    # main training/testing loop
    if args.train:
        for episode in trange(EPISODES, desc= "Training Episodes"):
            obs = env.reset()

            while not done:
                action = agent.act(obs)
                next_obs, rewards, done, info = env.step(action)                
                agent.observe(next_obs, rewards, done, info)
                env.render()

if __name__ == "__main__":
    parser = populate_parser(argparse.ArgumentParser(description="MARL Benchmark"))
    args, _ = parser.parse_known_args()
    main(args)
    
    