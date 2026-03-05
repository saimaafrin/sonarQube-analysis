from collections import defaultdict
from random import randint
def task_func(dict1):
    # Initialize a defaultdict to store department codes and their corresponding employee salaries
    department_salaries = defaultdict(list)
    
    # Iterate through the dictionary to populate the department_salaries dictionary
    for key, value in dict1.items():
        if key.startswith('EMP$$'):
            department_salaries[key] = value
    
    return department_salaries