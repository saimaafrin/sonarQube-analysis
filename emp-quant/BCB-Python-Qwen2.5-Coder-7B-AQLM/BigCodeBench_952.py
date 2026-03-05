
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
        raise ValueError("n_tasks cannot be negative")
    
    if seed is not None:
        random.seed(seed)
    
    # Sanitize task names by replacing spaces with underscores
    task_list = [task.replace(" ", "_") for task in task_list]
    
    # Set due date to the current system date
    due_date = datetime.now().strftime("%Y-%m-%d")
    
    # Randomly assign tasks to employees
    assigned_tasks = []
    for _ in range(n_tasks):
        task = random.choice(task_list)
        employee = random.choice(employees)
        assigned_tasks.append({"Task Name": task, "Assigned To": employee, "Due Date": due_date})
    
    # Create DataFrame from the assigned tasks
    df = pd.DataFrame(assigned_tasks)
    
    return df