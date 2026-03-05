import json
import os
def task_func(file_path):
    """
    Check that the data in a JSON file is a list of dictionaries (objects in JavaScript).
    The function should output with:
        bool: True if the data is a list of dictionaries, False otherwise.
    """
    # Open the JSON file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Check if the data is a list
    if not isinstance(data, list):
        return False

    # Check if all elements in the list are dictionaries
    for element in data:
        if not isinstance(element, dict):
            return False

    # If all checks pass, return True
    return True
file_path = 'data.json'