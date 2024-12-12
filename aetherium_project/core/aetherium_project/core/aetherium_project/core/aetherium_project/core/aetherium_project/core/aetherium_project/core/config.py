# aetherium_project/core/config.py
# Configuration settings for the simulation
import json

class Config:
    def __init__(self, settings_path="data/settings.json"):
        self.settings = json.load(open(settings_path, 'r'))

    def get_setting(self, key):
        return self.settings.get(key)
