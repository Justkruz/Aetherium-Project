# aetherium_project/experiments/experiment_1.py
from core.environment import Environment
from core.agent import Agent
from core.learning import LearningMechanism
import numpy as np
from core.config import Config

config = Config()
env_size = config.get_setting("environment_size")
env = Environment(size=env_size)
agent = Agent(name="TestAgent", x=0, y=0)
env.add_agent(agent)
learning = LearningMechanism()

for _ in range(config.get_setting("simulation_speed")):
    env.step()
    learning.learn(agent, env)
    env.render()
