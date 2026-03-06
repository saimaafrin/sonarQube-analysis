
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
    
    if seed is not None:
        random.seed(seed)
    
    # Sanitize task names
    task_list = [task.replace(' ', '_') for task in task_list]
    
    # Select random tasks without replacement
    selected_tasks = random.sample(task_list, min(n_tasks, len(task_list)))
    
    # Create a list of dictionaries to hold the data
    data = []
    for task in selected_tasks:
        employee = random.choice(employees)
        due_date = datetime.now().strftime('%Y-%m-%d')
        data.append({'Task Name': task, 'Assigned To': employee, 'Due Date': due_date})
    
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)
    
    return df