from collections import defaultdict
from random import randint
def task_func(dict1):
    # Create a defaultdict to store department codes and their corresponding employee salaries
    department_salaries = defaultdict(list)
    
    # Iterate through the input dictionary
    for key, value in dict1.items():
        # Check if the department code starts with 'EMP$$'
        if key.startswith('EMP$$'):
            # Add the employee salaries to the corresponding department code in the dictionary
            department_salaries[key].extend(value)
    
    # Return the dictionary with department codes and their corresponding employee salaries
    return dict(department_salaries)
dict1 = {
    'EMP$$101': [50000, 60000, 55000],
    'HR$$201': [45000, 48000],
    'EMP$$102': [52000, 53000],
    'IT$$301': [65000, 67000, 66000]
}