
import json
import os
import re

def task_func(
    file_path,
    attribute,
    INPUT_JSON={
        "type": "object",
        "properties": {
            "name": {"type": str},  
            "age": {"type": int},   
            "email": {"type": str}  
        },
        "required": ["name", "age", "email"]
    },
    EMAIL_REGEX=r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"):
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise ValueError("File does not exist")
    
    # Load the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Validate the structure and contents of the JSON file
    if not isinstance(data, dict):
        raise ValueError("Invalid JSON structure")
    
    for key, value in INPUT_JSON["properties"].items():
        if key not in data:
            raise ValueError(f"Required attribute '{key}' is missing")
        if not isinstance(data[key], value["type"]):
            raise ValueError(f"Type mismatch for attribute '{key}'")
        if key == "email" and not re.match(EMAIL_REGEX, data[key]):
            raise ValueError(f"Invalid email format for attribute '{key}'")
    
    # Retrieve the specified attribute
    if attribute not in data:
        raise ValueError(f"Attribute '{attribute}' not found in JSON data")
    
    return data[attribute]