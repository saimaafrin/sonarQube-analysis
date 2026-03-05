
import collections
import random
import json

# Constants
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']

def task_func(department_data):
    # Create a dictionary to store the employee levels for each department
    employee_levels = collections.defaultdict(list)
    
    # Iterate over the department data and populate the dictionary
    for department, count in department_data:
        # Generate random employee levels based on the count
        levels = random.choices(LEVELS, k=count)
        employee_levels[department].extend(levels)
    
    # Convert the dictionary to a JSON object
    json_object = json.dumps(employee_levels, indent=4)
    
    return json_object

print(task_func(department_data))