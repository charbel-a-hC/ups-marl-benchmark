ENV_CONFIG = {
  "controlled_vehicles": 3,
  "ego_spacing": 1,
  "observation": {
      "type": "MultiAgentObservation",
      "observation_config": {
          "type": "Kinematics",
          "vehicles_count": 10,
          "features": ["presence", "x", "y", "vx", "vy", "cos_h"],
          "features_range": {
              "x": [-600, 600],
              "y": [-100, 100],
              "vx": [-30, 30],
              "vy": [-30, 30]
          },
          "absolute": False,
          "normalize": False,
          "order": "sorted"
      }
  },
  "action": {
      "type": "MultiAgentAction",
      "action_config": {
          "type": "DiscreteMetaAction",
      }
  },
  "simulation_frequency": 60,
  "vehicles_count": 10,
  "vehicles_density": 5,
  "show_trajectories": False,
  "screen_width": 600,
  "screen_height": 300
}
