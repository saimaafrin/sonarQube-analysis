
from collections import defaultdict
from random import randint

def task_func(dict1):
    department_salaries = defaultdict(list)
    
    for key, value in dict1.items():
        if key.startswith('EMP$$'):
            department_salaries[key] = [randint(5000, 10000) for _ in range(value)]
    
    return dict(department_salaries)