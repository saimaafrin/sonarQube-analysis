
import random
from string import ascii_uppercase

def task_func(departments):
    employee_ids = {}
    for department, employees in departments.items():
        for employee in employees:
            employee_id = f"{department}{random.choice(ascii_uppercase[:5])}"
            employee_ids[employee_id] = employee
    return list(employee_ids.values())

print(task_func(departments))