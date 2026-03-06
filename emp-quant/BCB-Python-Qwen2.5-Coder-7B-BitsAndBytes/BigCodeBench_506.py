
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Convert the data list into a DataFrame
    df = pd.DataFrame(data)
    
    # Check if the DataFrame is empty
    if df.empty:
        return {
            'sum': np.nan,
            'mean': np.nan,
            'min': np.inf,
            'max': -np.inf,
            'plot': None
        }
    
    # Calculate the required statistics
    sum_value = df[column].sum()
    mean_value = df[column].mean()
    min_value = df[column].min()
    max_value = df[column].max()
    
    # Generate the histogram plot
    plot = df[column].hist(bins=10, figsize=(8, 6))
    
    # Return the results as a dictionary
    return {
        'sum': sum_value,
        'mean': mean_value,
        'min': min_value,
        'max': max_value,
        'plot': plot
    }

result = task_func('temperature', data)
print(result['sum'], result['mean'], result['min'], result['max'])
plt.show()