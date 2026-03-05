import collections
import random
import json
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']
def task_func(department_data):
    """
    Generate a JSON object from employee data based on given department codes and their employee counts.
    """
    # Create a dictionary to store the department data
    department_data_dict = {}

    # Iterate over the department data and add it to the dictionary
    for department, count in department_data:
        department_data_dict[department] = count

    # Create a list of lists to store the employee levels for each department
    employee_levels = []

    # Iterate over the departments and add the employee levels to the list
    for department in PREFICES:
        employee_levels.append([])
        for level in LEVELS:
            employee_levels[-1].append(department_data_dict.get(department, 0))

    # Convert the list of lists to a JSON object
    json_data = json.dumps(employee_levels)

    return json_data
department_data = [
    ('EMP$$', 10),
    ('MAN$$', 20),
    ('DEV$$', 30),
    ('HR$$', 40)
]