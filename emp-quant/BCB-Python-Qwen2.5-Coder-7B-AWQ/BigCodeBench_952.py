import pandas as pd
import random
from datetime import datetime
def task_func(
    task_list,
    n_tasks,
    employees=["John Doe", "Jane Smith", "James Brown", "Mary Johnson", "Robert Davis"],
    seed=None,
):
    """
    Randomly assigns a specified number of tasks to employees with a due date of the current day and returns a DataFrame with these assignments.
    
    Parameters:
    - task_list: List of task names.
    - n_tasks: Number of tasks to assign.
    - employees: List of employee names to assign tasks to.
    - seed: Seed for random number generator for reproducibility.
    
    Returns:
    - pd.DataFrame: Contains columns 'Task Name', 'Assigned To', and 'Due Date', with each row representing an assigned task.
    
    Raises:
    - ValueError: If n_tasks is negative.
    """
    if n_tasks < 0:
        raise ValueError("n_tasks must be a non-negative integer")
    
    if seed is not None:
        random.seed(seed)
    
    # Sanitize task names by replacing spaces with underscores
    task_list = [task.replace(" ", "_") for task in task_list]
    
    # Select a random subset of tasks
    selected_tasks = random.sample(task_list, min(n_tasks, len(task_list)))
    
    # Assign tasks to random employees
    assignments = []
    for task in selected_tasks:
        assigned_to = random.choice(employees)
        due_date = datetime.now().strftime("%Y-%m-%d")
        assignments.append({'Task Name': task, 'Assigned To': assigned_to, 'Due Date': due_date})
    
    # Create DataFrame from assignments
    df = pd.DataFrame(assignments)
    return df