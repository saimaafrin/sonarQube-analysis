
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Check for negative values in the column
    if data[column].lt(0).any():
        raise ValueError("Negative values are not allowed in the column.")
    
    # Calculate the sum, mean, min, and max of the column
    summary_stats = {
        'sum': data[column].sum(),
        'mean': data[column].mean(),
        'min': data[column].min(),
        'max': data[column].max()
    }
    
    # Create a bar chart for the given column
    fig, ax = plt.subplots()
    ax.bar(range(len(data)), data[column], tick_label=data.index)
    ax.set_xlabel('Product')
    ax.set_ylabel(column)
    ax.set_title(f'Bar Chart of {column}')
    
    # Return the summary statistics and the Axes object
    return summary_stats, ax