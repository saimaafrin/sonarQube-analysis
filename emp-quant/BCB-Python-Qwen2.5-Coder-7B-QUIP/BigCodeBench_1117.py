
import collections
import random
import json
# Constants
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']

def task_func(department_data):
    # Generate random employee levels for each department
    department_employees = collections.defaultdict(list)
    for _ in range(department_data):
        department_code = random.choice(PREFICES)
        employee_level = random.choice(LEVELS)
        department_employees[department_code].append(employee_level)

    # Convert to JSON and return
    return json.dumps(department_employees, indent=4)