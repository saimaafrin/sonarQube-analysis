
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
        raise ValueError("Invalid column name")
    
    # Calculate the required statistics
    result = {
        'sum': data[column].sum(),
        'mean': data[column].mean(),
        'min': data[column].min(),
        'max': data[column].max()
    }
    
    return result