
import json
import os

def task_func(file_path):
    with open(file_path, "r") as f:
        data = f.read()
    try:
        data = json.loads(data)
    except ValueError:
        return False
    if not isinstance(data, list):
        return False
    for d in data:
        if not isinstance(d, dict):
            return False
    return True