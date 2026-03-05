
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Check for negative values in the specified column
    if (df[column] < 0).any():
        raise ValueError("Quantity sold or total sales cannot be negative.")
    
    # Calculate the sum, mean, min, and max of the specified column
    stats = {
        'sum': df[column].sum(),
        'mean': df[column].mean(),
        'min': df[column].min(),
        'max': df[column].max()
    }
    
    # Create a bar chart plot for the specified column
    ax = df.plot(kind='bar', x='Product', y=column, legend=False)
    ax.set_title(f'Bar Chart of {column}')
    
    # Return the dictionary of statistics and the Axes object of the plot
    return stats, ax