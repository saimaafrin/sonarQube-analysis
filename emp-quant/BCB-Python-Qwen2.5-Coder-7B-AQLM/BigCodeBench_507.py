
import pandas as pd
import numpy as np

def task_func(column, data):
    # Check if the data is empty
    if data.empty:
        return {
            'sum': 0,
            'mean': np.nan,
            'min': np.nan,
            'max': np.nan
        }
    
    # Check if the specified column exists in the data
    if column not in data.columns:
        raise ValueError(f"Invalid column name: {column}")
    
    # Calculate the sum, mean, minimum, and maximum values for the specified column
    sum_value = data[column].sum()
    mean_value = data[column].mean()
    min_value = data[column].min()
    max_value = data[column].max()
    
    # Return the results in a dictionary
    return {
        'sum': sum_value,
        'mean': mean_value,
        'min': min_value,
        'max': max_value
    }