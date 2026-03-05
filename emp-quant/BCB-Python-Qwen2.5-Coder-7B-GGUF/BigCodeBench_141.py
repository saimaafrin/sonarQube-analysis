
import numpy as np
import pandas as pd
import statistics

def task_func(rows, columns=['A', 'B', 'C', 'D', 'E', 'F'], seed=42):
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("The 'rows' parameter must be a positive integer greater than 0.")
    
    np.random.seed(seed)
    data = {col: np.random.randint(1, 101, rows) for col in columns}
    df = pd.DataFrame(data)
    
    results = {col: {'mean': df[col].mean(), 'median': df[col].median()} for col in columns}
    
    return df, results