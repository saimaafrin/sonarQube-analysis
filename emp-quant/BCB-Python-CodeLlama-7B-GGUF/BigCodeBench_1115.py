
import random
from string import ascii_uppercase

def generate_employee_id(department_code):
    """
    Generate a unique employee ID based on the department code.

    Args:
        department_code (str): The department code.

    Returns:
        str: The generated employee ID.
    """
    random_string = ''.join(random.choice(ascii_uppercase) for _ in range(5))
    return f"{department_code}-{random_string}"

def task_func(departments):
    """
    Assign a unique employee ID to each employee in the company.

    Args:
        departments (dict): A dictionary of department codes and their corresponding employees.

    Returns:
        list: A list of unique employee IDs for all departments.
    """
    employee_ids = []
    for department_code, employees in departments.items():
        for employee in employees:
            employee_ids.append(generate_employee_id(department_code))
    return employee_ids

employee_ids = task_func(departments)
print(employee_ids)