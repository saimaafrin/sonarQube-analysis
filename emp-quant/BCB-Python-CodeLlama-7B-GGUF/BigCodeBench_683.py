
import math
import yaml

def task_func(yaml_path, key):
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)

    data[key] = math.cos(data[key])

    with open(yaml_path, 'w') as f:
        yaml.dump(data, f)

    return data