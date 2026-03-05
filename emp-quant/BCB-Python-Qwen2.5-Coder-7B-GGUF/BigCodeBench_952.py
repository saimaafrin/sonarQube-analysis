
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
    
    # Filter tasks to only include those that are due today
    today = datetime.now().date()
    due_today_tasks = [task for task in task_list if task.endswith(f"_{today}")]

    if n_tasks > len(due_today_tasks):
        raise ValueError("Not enough tasks due today to assign the specified number of tasks")
    
    # Randomly select n_tasks from the due today tasks
    selected_tasks = random.sample(due_today_tasks, n_tasks)
    
    # Assign tasks to employees
    assignments = []
    for task in selected_tasks:
        employee = random.choice(employees)
        assignments.append({
            'Task Name': task,
            'Assigned To': employee,
            'Due Date': today
        })
    
    # Create DataFrame from assignments
    df = pd.DataFrame(assignments)
    return df