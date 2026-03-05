
import collections
import random
import json

# Constants
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']

def task_func(department_data):
    # Initialize an empty dictionary to store the department data
    department_data_dict = {}

    # Iterate over the department codes and their employee counts
    for department_code, employee_count in department_data:
        # Initialize a list to store the employee levels for this department
        employee_levels = []

        # Generate random employee levels for this department
        for _ in range(employee_count):
            employee_levels.append(random.choice(LEVELS))

        # Add the department data to the dictionary
        department_data_dict[department_code] = employee_levels

    # Convert the dictionary to a JSON object
    json_data = json.dumps(department_data_dict)

    # Return the JSON object
    return json_data