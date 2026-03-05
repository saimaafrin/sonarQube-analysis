
import json
import os
import re

def task_func(file_path, attribute, INPUT_JSON, EMAIL_REGEX):
    if not os.path.exists(file_path):
        raise ValueError("File does not exist")
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    if not all(key in data for key in INPUT_JSON['required']):
        raise ValueError("Missing required attributes")
    
    for key, value in INPUT_JSON['properties'].items():
        if key in data and not isinstance(data[key], value['type']):
            raise ValueError(f"Invalid type for {key}")
    
    if not re.match(EMAIL_REGEX, data['email']):
        raise ValueError("Invalid email format")
    
    return data[attribute]