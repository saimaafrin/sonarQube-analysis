
import numpy as np
import pandas as pd
import statistics

def task_func(rows, columns=['A', 'B', 'C', 'D', 'E', 'F'], seed=42):
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("The 'rows' parameter must be a positive integer greater than 0.")
    
    np.random.seed(seed)
    data = {col: np.random.randint(1, 101, rows) for col in columns}
    df = pd.DataFrame(data)
    
    results = {}
    for col in columns:
        mean_value = df[col].mean()
        median_value = df[col].median()
        results[col] = {'mean': mean_value, 'median': median_value}
    
    return df, results