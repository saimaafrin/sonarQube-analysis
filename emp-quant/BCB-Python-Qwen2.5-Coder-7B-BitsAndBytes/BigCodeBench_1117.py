
import collections
import random
import json

# Constants
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']

def task_func(department_data):
    # Create a dictionary to store the employee levels for each department
    department_levels = {prefix: [] for prefix in PREFICES}
    
    # Populate the dictionary with random employee levels
    for _ in range(department_data):
        prefix = random.choice(PREFICES)
        level = random.choice(LEVELS)
        department_levels[prefix].append(level)
    
    # Convert the dictionary to a JSON string
    json_output = json.dumps(department_levels, indent=4)
    
    return json_output