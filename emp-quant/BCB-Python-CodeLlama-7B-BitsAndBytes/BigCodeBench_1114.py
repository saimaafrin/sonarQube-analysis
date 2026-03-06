
from collections import defaultdict
from random import randint

def task_func(dict1):
    # Create a dictionary to store the employee data
    employee_data = defaultdict(list)

    # Generate some random employee data
    for i in range(10):
        department_code = f"EMP$${randint(100, 999)}"
        salary = randint(50000, 100000)
        employee_data[department_code].append(salary)

    # Print the employee data
    print(employee_data)

# Call the function
task_func(None)