
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Check if the data contains negative values in the specified column
    if data[column].lt(0).any():
        raise ValueError("Quantity sold or total sales cannot be negative.")
    
    # Calculate the sum, mean, min, and max of the specified column
    stats = {
        'sum': data[column].sum(),
        'mean': data[column].mean(),
        'min': data[column].min(),
        'max': data[column].max()
    }
    
    # Create a bar chart plot for the specified column
    fig, ax = plt.subplots()
    ax.bar(data['Product'], data[column])
    ax.set_title(f'Bar Chart of {column}')
    ax.set_xlabel('Product')
    ax.set_ylabel(column)
    
    # Return the dictionary of statistics and the Axes object of the bar chart
    return stats, ax