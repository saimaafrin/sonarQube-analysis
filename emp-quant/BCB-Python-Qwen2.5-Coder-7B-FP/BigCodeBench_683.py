import math
import yaml
def task_func(yaml_path, key):
    # Read the YAML file
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
    
    # Apply the cosine to the specific key
    if key in data:
        data[key] = math.cos(data[key])
    
    # Write the modified data back into the YAML file
    with open(yaml_path, 'w') as file:
        yaml.safe_dump(data, file)
    
    return data