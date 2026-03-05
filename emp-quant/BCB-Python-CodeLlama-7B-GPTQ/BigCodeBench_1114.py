from collections import defaultdict
from random import randint
def task_func(dict1):
    """
    Create a dictionary of employee data for departments starting with 'EMP$$'.
    The keys are department codes and the values are lists of the salaries of employees in that department.
    """
    # Initialize an empty dictionary
    emp_dict = defaultdict(list)

    # Generate random department codes and salaries
    for i in range(10):
        dept_code = f"EMP{randint(100, 999)}"
        salary = randint(10000, 100000)
        emp_dict[dept_code].append(salary)

    # Print the dictionary
    print(emp_dict)
dict1 = {
    "EMP100": [10000, 20000, 30000],
    "EMP200": [40000, 50000, 60000],
    "EMP300": [70000, 80000, 90000],
}