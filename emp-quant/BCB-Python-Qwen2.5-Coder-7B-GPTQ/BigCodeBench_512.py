import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(column, data):
    # Convert data to DataFrame
    df = pd.DataFrame(data)
    
    # Check for negative values in the specified column
    if df[column].min() < 0:
        raise ValueError("Negative values are not allowed in the specified column.")
    
    # Calculate sum, mean, min, and max of the specified column
    stats = {
        'sum': df[column].sum(),
        'mean': df[column].mean(),
        'min': df[column].min(),
        'max': df[column].max()
    }
    
    # Create a bar chart plot
    fig, ax = plt.subplots()
    ax.bar(df['Product'], df[column])
    ax.set_title(f'Bar Chart of {column}')
    ax.set_xlabel('Product')
    ax.set_ylabel(column)
    
    # Return the dictionary of statistics and the Axes object
    return stats, ax