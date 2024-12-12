# aetherium_project/tests/test_agent.py
import unittest
from core.agent import Agent
from core.environment import Environment

class TestAgent(unittest.TestCase):
    def test_agent_creation(self):
        agent = Agent(name="TestAgent", x=0, y=0)
        self.assertEqual(agent.name, "TestAgent")
        self.assertEqual(agent.x, 0)
        self.assertEqual(agent.y, 0)
    def test_agent_movement(self):
        agent = Agent(name="TestAgent", x=0, y=0)
        env = Environment(size=5)
        agent.act(env)
        self.assertTrue(agent.x >= 0 and agent.x < env.size)
        self.assertTrue(agent.y >= 0 and agent.y < env.size)
