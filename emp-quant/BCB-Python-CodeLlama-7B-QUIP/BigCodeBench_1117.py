
import collections
import random
import json
# Constants
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']
def task_func(department_data):
    # Initialize the JSON object
    json_obj = {}
    # Loop through the departments
    for department in PREFICES:
        # Get the number of employees in this department
        num_employees = department_data[department]
        # Choose a random number of employees to be in the 'Junior' level
        num_juniors = random.randint(0, num_employees)
        # Choose a random number of employees to be in the 'Mid' level
        num_mids = random.randint(0, num_employees - num_juniors)
        # Choose a random number of employees to be in the 'Senior' level
        num_seniors = num_employees - num_juniors - num_mids
        # Add the levels to the JSON object
        json_obj[department] = {
            'Junior': num_juniors,
            'Mid': num_mids,
            'Senior': num_seniors
        }
    # Return the JSON object
    return json.dumps(json_obj)