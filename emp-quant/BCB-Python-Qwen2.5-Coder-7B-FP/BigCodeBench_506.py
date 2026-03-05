import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(column, data):
    # Convert the data list into a DataFrame
    df = pd.DataFrame(data, columns=['date', 'temperature', 'humidity', 'wind speed', 'precipitation'])
    
    # Check if the DataFrame is empty
    if df.empty:
        return {
            'sum': np.nan,
            'mean': np.nan,
            'min': np.inf,
            'max': -np.inf,
            'plot': None
        }
    
    # Calculate the sum, mean, min, and max of the specified column
    sum_value = df[column].sum()
    mean_value = df[column].mean()
    min_value = df[column].min()
    max_value = df[column].max()
    
    # Generate a histogram plot of the specified column
    plot = df[column].hist(bins=10, figsize=(8, 6))
    
    # Return the result as a dictionary
    return {
        'sum': sum_value,
        'mean': mean_value,
        'min': min_value,
        'max': max_value,
        'plot': plot
    }