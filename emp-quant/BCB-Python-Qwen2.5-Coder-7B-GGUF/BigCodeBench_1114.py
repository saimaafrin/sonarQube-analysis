
from collections import defaultdict
from random import randint

def task_func(dict1):
    department_salaries = defaultdict(list)
    
    for key, value in dict1.items():
        if key.startswith('EMP$$'):
            for employee_salary in value:
                department_salaries[key].append(employee_salary)
    
    return dict(department_salaries)

result = task_func(employee_data)
print(result)