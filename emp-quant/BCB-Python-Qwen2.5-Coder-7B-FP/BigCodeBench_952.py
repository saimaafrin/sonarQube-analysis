import pandas as pd
import random
from datetime import datetime
def task_func(
    task_list,
    n_tasks,
    employees=["John Doe", "Jane Smith", "James Brown", "Mary Johnson", "Robert Davis"],
    seed=None,
):
    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)
    
    # Check if n_tasks is negative
    if n_tasks < 0:
        raise ValueError("n_tasks cannot be negative")
    
    # Sanitize task names by replacing spaces with underscores
    sanitized_tasks = [task.replace(" ", "_") for task in task_list]
    
    # Get the current system date
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Randomly select n_tasks from the sanitized task list
    selected_tasks = random.sample(sanitized_tasks, n_tasks)
    
    # Randomly assign the selected tasks to employees
    assignments = [(task, random.choice(employees), current_date) for task in selected_tasks]
    
    # Create a DataFrame with the assignments
    df = pd.DataFrame(assignments, columns=['Task Name', 'Assigned To', 'Due Date'])
    
    return df