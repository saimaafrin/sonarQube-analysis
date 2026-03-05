import json
import os
def task_func(file_path):
    """
    Check that the data in a JSON file is a list of dictionaries (objects in JavaScript).
    The function should output with:
        bool: True if the data is a list of dictionaries, False otherwise.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        return False
    if not isinstance(data, list):
        return False
    for item in data:
        if not isinstance(item, dict):
            return False
    return True
file_path = 'data.json'