
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
    
    # Sanitize task names
    task_list = [task.replace(" ", "_") for task in task_list]
    
    # Set the seed for random number generation
    if seed is not None:
        random.seed(seed)
    
    # Assign tasks to employees
    assigned_tasks = []
    for _ in range(n_tasks):
        task = random.choice(task_list)
        assigned_to = random.choice(employees)
        assigned_tasks.append({
            'Task Name': task,
            'Assigned To': assigned_to,
            'Due Date': datetime.now().strftime('%Y-%m-%d')
        })
    
    # Create DataFrame
    df = pd.DataFrame(assigned_tasks)
    
    return df