
import math
import yaml

def task_func(yaml_path, key):
    # Read the YAML file
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
    
    # Check if the key exists in the data
    if key not in data:
        raise KeyError(f"Key '{key}' not found in the YAML data.")
    
    # Apply the cosine function to the value associated with the key
    data[key] = math.cos(data[key])
    
    # Write the modified data back to the YAML file
    with open(yaml_path, 'w') as file:
        yaml.safe_dump(data, file)
    
    return data