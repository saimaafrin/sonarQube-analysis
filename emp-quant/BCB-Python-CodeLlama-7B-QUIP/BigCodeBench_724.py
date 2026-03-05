
import os
import json

def task_func(config_path: str) -> dict:
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file {config_path} does not exist.")
    with open(config_path, "r") as f:
        config = json.load(f)
    return config