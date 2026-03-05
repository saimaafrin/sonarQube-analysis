import os
import json
def task_func(config_path: str) -> dict:
    """
    Load a JSON configuration file and return the configuration dictionary.

    Args:
        config_path (str): Path to the configuration file.

    Returns:
        config (dict): Configuration dictionary loaded from the file.

    Raises:
        FileNotFoundError: If the provided configuration file does not exist.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file {config_path} does not exist.")

    with open(config_path, "r") as f:
        config = json.load(f)

    return config
config_path = "config.json"