
import random
from string import ascii_uppercase

def task_func(dict1):
    employee_ids = []
    for department, _ in dict1.items():
        for _ in range(10):  # Assuming each department has 10 employees
            random_string = ''.join(random.choices(ascii_uppercase, k=5))
            employee_ids.append(f"{department}{random_string}")
    return employee_ids