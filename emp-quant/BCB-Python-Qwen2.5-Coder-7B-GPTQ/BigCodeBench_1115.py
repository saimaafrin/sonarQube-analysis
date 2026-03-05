import random
from string import ascii_uppercase
def task_func(dict1):
    employee_ids = []
    used_ids = set()
    
    for department, num_employees in dict1.items():
        for _ in range(num_employees):
            unique_id = department + ''.join(random.choice(ascii_uppercase) for _ in range(5))
            while unique_id in used_ids:
                unique_id = department + ''.join(random.choice(ascii_uppercase) for _ in range(5))
            used_ids.add(unique_id)
            employee_ids.append(unique_id)
    
    return employee_ids