# aetherium_project/core/utils.py
# Generic utility functions go here
import json

def load_config(file_path):
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config
