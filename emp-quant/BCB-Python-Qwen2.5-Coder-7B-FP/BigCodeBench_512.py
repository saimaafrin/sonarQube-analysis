import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(column, data):
    # Convert data to DataFrame
    df = pd.DataFrame(data)
    
    # Check for negative values in the specified column
    if df[column].min() < 0:
        raise ValueError("Negative values found in the specified column.")
    
    # Calculate sum, mean, min, and max of the specified column
    stats = {
        'sum': df[column].sum(),
        'mean': df[column].mean(),
        'min': df[column].min(),
        'max': df[column].max()
    }
    
    # Create a bar chart for the specified column
    ax = df.plot(kind='bar', x='Product', y=column, title=f'Bar Chart of {column}')
    
    # Return the dictionary of statistics and the Axes object
    return stats, ax