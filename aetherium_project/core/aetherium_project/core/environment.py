# aetherium_project/core/environment.py
import numpy as np
class Environment:
    def __init__(self, size=10):
        self.size = size
        self.grid = np.zeros((size, size))
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def step(self):
        for agent in self.agents:
            agent.act(self)

    def render(self):
        print(self.grid)
