
import json
import os

def task_func(file_path):
    if not os.path.exists(file_path):
        return False

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                return True
            else:
                return False
    except json.JSONDecodeError:
        return False