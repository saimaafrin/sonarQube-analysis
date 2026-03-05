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
    
    for key, value in INPUT_JSON['properties'].items():
        if key not in data:
            raise ValueError(f"Missing required attribute: {key}")
        if not isinstance(data[key], value['type']):
            raise ValueError(f"Type mismatch for attribute {key}: expected {value['type'].__name__}, got {type(data[key]).__name__}")
    
    # Validate email format
    if 'email' in data and not re.match(EMAIL_REGEX, data['email']):
        raise ValueError("Invalid email format")
    
    # Retrieve the specified attribute
    return data.get(attribute, None)