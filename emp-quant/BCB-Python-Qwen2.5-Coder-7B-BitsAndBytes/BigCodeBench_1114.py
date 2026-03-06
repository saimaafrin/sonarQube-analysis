
from collections import defaultdict
from random import randint

def task_func(dict1):
    # Create a defaultdict to store department codes and their corresponding employee salaries
    department_salaries = defaultdict(list)
    
    # Iterate through the input dictionary
    for key, value in dict1.items():
        # Check if the key starts with 'EMP$$'
        if key.startswith('EMP$$'):
            # Append the salary to the list of the corresponding department
            department_salaries[key].append(value)
    
    return dict(department_salaries)

result = task_func(input_dict)
print(result)  # Output: {'EMP$$001': [5000], 'EMP$$002': [6000], 'EMP$$003': [7000], 'EMP$$005': [9000]}