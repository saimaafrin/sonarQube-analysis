import random
from string import ascii_uppercase
def task_func(dict1):
    employee_ids = []
    used_ids = set()
    
    for department, count in dict1.items():
        for _ in range(count):
            while True:
                random_string = ''.join(random.choice(ascii_uppercase) for _ in range(5))
                employee_id = f"{department}{random_string}"
                if employee_id not in used_ids:
                    used_ids.add(employee_id)
                    employee_ids.append(employee_id)
                    break
    
    return employee_ids