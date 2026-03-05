
from collections import defaultdict
from random import randint

def task_func(dict1):
    # Initialize an empty dictionary to store the employee data
    employee_data = defaultdict(list)

    # Generate random department codes starting with 'EMP$$'
    for i in range(10):
        department_code = f"EMP$${randint(100, 999)}"

        # Generate random employee salaries for each department
        for j in range(randint(1, 10)):
            employee_salary = randint(10000, 100000)
            employee_data[department_code].append(employee_salary)

    return employee_data