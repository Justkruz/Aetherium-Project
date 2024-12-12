# aetherium_project/tests/test_environment.py
import unittest
from core.environment import Environment
import numpy as np

class TestEnvironment(unittest.TestCase):
    def test_environment_creation(self):
        env = Environment(size=5)
        self.assertEqual(env.size, 5)
        self.assertEqual(env.grid.shape, (5, 5))
        self.assertTrue(np.all(env.grid == 0))
