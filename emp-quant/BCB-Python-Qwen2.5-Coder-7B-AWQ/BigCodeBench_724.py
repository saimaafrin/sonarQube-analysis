import os
import json
def task_func(config_path: str) -> dict:
    """
    Load a JSON configuration file and return the configuration dictionary.
    
    Args:
        config_path (str): The path to the JSON configuration file.
    
    Returns:
        config (dict): Configuration dictionary loaded from the file.
    
    Raises:
        FileNotFoundError: If the provided configuration file does not exist.
    """
    # Check if the file exists
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"The file {config_path} does not exist.")
    
    # Load the JSON configuration file
    with open(config_path, 'r') as file:
        config = json.load(file)
    
    return config