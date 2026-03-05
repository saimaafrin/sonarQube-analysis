import collections
import random
import json
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']
def task_func(department_data):
    # Create a dictionary to store the employee levels for each department
    employee_levels = {prefix: [] for prefix in PREFICES}
    
    # Populate the dictionary with random employee levels based on the given department counts
    for prefix, count in department_data.items():
        for _ in range(count):
            employee_levels[prefix].append(random.choice(LEVELS))
    
    # Convert the dictionary to a JSON object
    json_object = json.dumps(employee_levels, indent=4)
    
    return json_object