import os
import json
def task_func(config_path: str) -> dict:
    """
    Load a JSON configuration file and return the configuration dictionary.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file {config_path} does not exist.")

    with open(config_path, "r") as f:
        config = json.load(f)

    return config
config_path = "config.json"