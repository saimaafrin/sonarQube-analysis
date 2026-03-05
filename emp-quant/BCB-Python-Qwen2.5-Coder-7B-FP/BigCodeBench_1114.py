from collections import defaultdict
from random import randint
def task_func(dict1):
    # Create a defaultdict to store department codes and their corresponding employee salaries
    department_salaries = defaultdict(list)
    
    # Iterate through the input dictionary
    for key, value in dict1.items():
        # Check if the department code starts with 'EMP$$'
        if key.startswith('EMP$$'):
            # Append the employee's salary to the corresponding department list
            department_salaries[key].append(value)
    
    # Return the dictionary containing department codes and their employee salaries
    return dict(department_salaries)