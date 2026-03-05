
import pandas as pd
import random
from datetime import datetime

def task_func(
    task_list,
    n_tasks,
    employees=["John Doe", "Jane Smith", "James Brown", "Mary Johnson", "Robert Davis"],
    seed=None,
):
    if n_tasks < 0:
        raise ValueError("n_tasks must be a non-negative integer")

    # Sanitize task names by replacing spaces with underscores
    task_list = [task.replace(" ", "_") for task in task_list]

    # Set due date to current system date
    due_date = datetime.today().strftime("%Y-%m-%d")

    # Randomly assign tasks to employees
    assigned_tasks = random.sample(task_list, n_tasks)
    assigned_employees = random.sample(employees, n_tasks)

    # Create DataFrame with assigned tasks and employees
    df = pd.DataFrame(
        {
            "Task Name": assigned_tasks,
            "Assigned To": assigned_employees,
            "Due Date": [due_date] * n_tasks,
        }
    )

    return df