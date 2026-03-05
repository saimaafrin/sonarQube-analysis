
import random
from string import ascii_uppercase

def generate_unique_id(department_code):
    random_string = ''.join(random.choice(ascii_uppercase) for _ in range(5))
    return f"{department_code}{random_string}"

def task_func(dict1):
    unique_ids = {}
    for department in dict1:
        unique_ids[department] = generate_unique_id(department)
    return unique_ids