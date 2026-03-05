
import os
import json

def task_func(config_path: str) -> dict:
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"The configuration file at {config_path} does not exist.")
    
    with open(config_path, 'r') as file:
        config = json.load(file)
    
    return config