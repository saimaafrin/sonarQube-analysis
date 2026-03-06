
import random
from string import ascii_uppercase

def task_func(dict1):
    employee_ids = []
    for dept_code, num_employees in dict1.items():
        for _ in range(num_employees):
            random_string = ''.join(random.choices(ascii_uppercase, k=5))
            employee_id = f"{dept_code}{random_string}"
            employee_ids.append(employee_id)
    return employee_ids