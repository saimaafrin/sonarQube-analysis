
from collections import defaultdict
from random import randint

def task_func(dict1):
    # Create a dictionary of employee data for departments starting with 'EMP$$'
    emp_data = defaultdict(list)
    for i in range(10):
        emp_data[f"EMP$${i}"] = [randint(1000, 5000)]
    return emp_data