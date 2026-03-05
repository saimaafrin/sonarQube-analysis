
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    if not data:
        return {
            'sum': np.nan,
            'mean': np.nan,
            'min': np.inf,
            'max': -np.inf,
            'plot': None
        }
    
    # Convert data to DataFrame
    df = pd.DataFrame(data)
    
    # Calculate statistical properties
    sum_value = df[column].sum()
    mean_value = df[column].mean()
    min_value = df[column].min()
    max_value = df[column].max()
    
    # Generate histogram plot
    plot = df[column].hist(bins=10, figsize=(10, 6))
    
    # Return the results
    return {
        'sum': sum_value,
        'mean': mean_value,
        'min': min_value,
        'max': max_value,
        'plot': plot
    }