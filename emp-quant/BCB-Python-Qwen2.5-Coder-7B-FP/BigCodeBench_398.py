import json
import os
def task_func(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        return False
    
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Check if the data is a list
    if not isinstance(data, list):
        return False
    
    # Check if all items in the list are dictionaries
    for item in data:
        if not isinstance(item, dict):
            return False
    
    return True