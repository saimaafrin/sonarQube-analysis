import collections
import random
import json
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']
def task_func(department_data):
    # Create a dictionary to store employee levels for each department
    department_levels = {prefix: [] for prefix in PREFICES}
    
    # Populate the dictionary with random employee levels based on the given department counts
    for prefix, count in department_data.items():
        for _ in range(count):
            department_levels[prefix].append(random.choice(LEVELS))
    
    # Convert the dictionary to a JSON object
    json_object = json.dumps(department_levels, indent=4)
    
    return json_object
department_data = {
    'EMP$$': 5,
    'MAN$$': 3,
    'DEV$$': 7,
    'HR$$': 2
}