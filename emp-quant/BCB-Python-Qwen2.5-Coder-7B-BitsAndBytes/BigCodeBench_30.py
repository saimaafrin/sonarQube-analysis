
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
    
    try:
        # Load the JSON data from the file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Validate the structure and contents of the JSON data
        if not isinstance(data, dict):
            raise ValueError("JSON data must be an object")
        
        for key, value in INPUT_JSON["properties"].items():
            if key not in data:
                raise ValueError(f"Required attribute '{key}' is missing")
            if not isinstance(data[key], value["type"]):
                raise ValueError(f"Attribute '{key}' must be of type {value['type'].__name__}")
        
        if "email" in data and not re.match(EMAIL_REGEX, data["email"]):
            raise ValueError("Invalid email format")
        
        # Retrieve the specified attribute
        return data.get(attribute, None)
    
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format")