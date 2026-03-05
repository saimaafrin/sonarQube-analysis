import collections
import random
import json
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']
def task_func(department_data):
    # Initialize a dictionary to store the department data
    department_levels = {prefix: [] for prefix in PREFICES}
    
    # Populate the dictionary with random employee levels
    for _ in range(department_data):
        prefix = random.choice(PREFICES)
        level = random.choice(LEVELS)
        department_levels[prefix].append(level)
    
    # Convert the dictionary to a JSON object
    json_object = json.dumps(department_levels, indent=4)
    
    return json_object