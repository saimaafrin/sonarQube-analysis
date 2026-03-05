
from collections import defaultdict
from random import randint
def task_func(dict1):
    # Create a dictionary to store department codes and their corresponding employee salaries
    department_salaries = defaultdict(list)

    # Iterate through the dictionary and add employee salaries to the appropriate department
    for key, value in dict1.items():
        if key.startswith('EMP$$'):
            for employee_salary in value:
                department_salaries[key].append(employee_salary)

    # Output the resulting dictionary
    return dict(department_salaries)