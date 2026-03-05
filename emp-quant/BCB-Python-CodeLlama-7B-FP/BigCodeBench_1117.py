import collections
import random
import json
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
def task_func(department_data):
    """
    Generate a JSON object from employee data based on given department codes and their employee counts.
    """
    # Initialize an empty dictionary to store the department data
    department_data_dict = {}

    # Iterate over the department data
    for department, count in department_data:
        # Check if the department is in the list of valid departments
        if department in PREFICES:
            # Add the department to the dictionary with the corresponding employee count
            department_data_dict[department] = count

    # Convert the dictionary to a JSON object
    json_data = json.dumps(department_data_dict)

    # Return the JSON object
    return json_data
department_data = [
    ('EMP$$', 10),
    ('MAN$$', 20),
    ('DEV$$', 30),
    ('HR$$', 40),
]