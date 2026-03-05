
import numpy as np
import pandas as pd
import statistics

def task_func(rows, columns=['A', 'B', 'C', 'D', 'E', 'F'], seed=42):
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("rows must be a positive integer greater than 0")
    
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Create a DataFrame with random numbers between 1 and 100
    data = {col: np.random.randint(1, 101, size=rows) for col in columns}
    df = pd.DataFrame(data)
    
    # Calculate the mean and median for each column
    stats = {col: {'mean': df[col].mean(), 'median': df[col].median()} for col in columns}
    
    return df, stats