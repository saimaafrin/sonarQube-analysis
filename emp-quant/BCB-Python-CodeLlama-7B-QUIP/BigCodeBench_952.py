
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
        raise ValueError("n_tasks must be non-negative")

    # Set the seed for random assignment
    if seed:
        random.seed(seed)

    # Create a list of task names
    task_names = [f"Task {i}" for i in range(n_tasks)]

    # Assign tasks to employees
    assigned_tasks = random.sample(task_names, n_tasks)

    # Create a DataFrame with the assigned tasks
    assigned_tasks_df = pd.DataFrame(
        {
            "Task Name": assigned_tasks,
            "Assigned To": random.choice(employees),
            "Due Date": datetime.today().date(),
        }
    )

    return assigned_tasks_df