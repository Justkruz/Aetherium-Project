# aetherium_project/main.py
from experiments.experiment_1 import config
from experiments.experiment_1 import env
from experiments.experiment_1 import learning
from experiments.experiment_1 import agent

print("Running experiment_1 with following settings:")
print(config.settings)
for _ in range(config.get_setting("simulation_speed")):
    env.step()
    learning.learn(agent, env)
    env.render()
