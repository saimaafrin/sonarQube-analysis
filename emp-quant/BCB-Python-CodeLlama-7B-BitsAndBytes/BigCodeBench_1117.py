
import collections
import random
import json

# Constants
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']

def task_func(department_data):
    # Create a dictionary to store the employee levels for each department
    employee_levels = collections.defaultdict(list)

    # Loop through the department data and add the employee levels to the dictionary
    for department, count in department_data.items():
        employee_levels[department].append(random.choice(LEVELS))

    # Convert the dictionary to a JSON object
    json_obj = json.dumps(employee_levels)

    # Return the JSON object
    return json_obj