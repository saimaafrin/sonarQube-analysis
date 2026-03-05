import collections
import random
import json
LEVELS = ['Junior', 'Mid', 'Senior']
def task_func(department_data):
    """
    Generate a JSON object from employee data based on given department codes and their employee counts.
    """
    # Initialize an empty dictionary to store the department data
    department_data_dict = {}

    # Iterate over the department codes and employee counts
    for department, count in department_data:
        # Initialize an empty list to store the employee levels
        employee_levels = []

        # Generate random employee levels for the current department
        for _ in range(count):
            employee_levels.append(random.choice(LEVELS))

        # Add the department data to the dictionary
        department_data_dict[department] = employee_levels

    # Convert the dictionary to a JSON object
    json_data = json.dumps(department_data_dict)

    # Return the JSON object
    return json_data
department_data = [
    ('EMP$$', 5),
    ('MAN$$', 3),
    ('DEV$$', 7),
    ('HR$$', 2),
]