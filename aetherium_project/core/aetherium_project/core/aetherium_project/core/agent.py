# aetherium_project/core/agent.py

class Agent:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def act(self, environment):
        # Placeholder action: Agent moves randomly
        dx = [-1, 0, 1, 0][np.random.randint(0, 4)]
        dy = [0, 1, 0, -1][np.random.randint(0, 4)]
        self.x = max(0, min(environment.size - 1, self.x + dx))
        self.y = max(0, min(environment.size - 1, self.y + dy))
