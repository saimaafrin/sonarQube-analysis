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
    
    if seed is not None:
        random.seed(seed)
    
    # Sanitize task names by replacing spaces with underscores
    task_list = [task.replace(" ", "_") for task in task_list]
    
    # Get the current date
    due_date = datetime.now().strftime("%Y-%m-%d")
    
    # Randomly select tasks
    selected_tasks = random.sample(task_list, min(n_tasks, len(task_list)))
    
    # Randomly assign tasks to employees
    assignments = []
    for task in selected_tasks:
        assigned_to = random.choice(employees)
        assignments.append({
            'Task Name': task,
            'Assigned To': assigned_to,
            'Due Date': due_date
        })
    
    # Create DataFrame
    df = pd.DataFrame(assignments)
    
    return df