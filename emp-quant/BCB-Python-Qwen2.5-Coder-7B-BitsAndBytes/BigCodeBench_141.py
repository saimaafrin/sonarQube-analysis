
import numpy as np
import pandas as pd

def task_func(rows, columns=['A', 'B', 'C', 'D', 'E', 'F'], seed=42):
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("The 'rows' parameter must be a positive integer greater than 0.")
    
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Create a DataFrame with random integers between 1 and 100
    data = {col: np.random.randint(1, 101, size=rows) for col in columns}
    df = pd.DataFrame(data)
    
    # Calculate mean and median for each column
    results = {}
    for col in columns:
        mean_value = df[col].mean()
        median_value = df[col].median()
        results[col] = {'mean': mean_value, 'median': median_value}
    
    return df, results