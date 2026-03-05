from collections import defaultdict
from random import randint
def task_func(dict1):
    """
    Create a dictionary of employee data for departments starting with 'EMP$$'.
    The keys are department codes and the values are lists of the salaries of employees in that department.
    """
    # Create a dictionary to store the employee data
    emp_data = defaultdict(list)

    # Generate some random employee data
    for i in range(10):
        emp_data['EMP$$' + str(i)].append(randint(1000, 5000))

    # Return the employee data dictionary
    return emp_data