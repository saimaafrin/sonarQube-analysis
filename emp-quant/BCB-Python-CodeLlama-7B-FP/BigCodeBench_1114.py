from collections import defaultdict
from random import randint
def task_func(dict1):
    """
    Create a dictionary of employee data for departments starting with 'EMP$$'.
    The keys are department codes and the values are lists of the salaries of employees in that department.
    """
    # Initialize an empty dictionary to store the results
    result = defaultdict(list)

    # Generate random department codes and salaries
    for i in range(10):
        department = f"EMP$${randint(100, 999)}"
        salary = randint(10000, 100000)
        result[department].append(salary)

    return result
dict1 = {
    "EMP123": [10000, 20000, 30000],
    "EMP456": [40000, 50000, 60000],
    "EMP789": [70000, 80000, 90000],
}