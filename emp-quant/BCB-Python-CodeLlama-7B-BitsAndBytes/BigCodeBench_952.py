
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
        raise ValueError("n_tasks must be a positive integer")

    # Create a list of tasks with sanitized names
    tasks = [f"Task {i+1}" for i in range(n_tasks)]

    # Create a list of employees with sanitized names
    employees = [f"{name.replace(' ', '_')}" for name in employees]

    # Create a list of due dates for the tasks
    due_dates = [datetime.today() for _ in range(n_tasks)]

    # Create a list of assignments with randomized tasks, employees, and due dates
    assignments = [
        {
            "Task Name": task,
            "Assigned To": random.choice(employees),
            "Due Date": due_date,
        }
        for task, due_date in zip(tasks, due_dates)
    ]

    # Create a DataFrame with the assignments
    df = pd.DataFrame(assignments)

    return df

df = task_func(task_list, n_tasks, employees, seed)
print(df)