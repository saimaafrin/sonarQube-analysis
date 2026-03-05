
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Check if the data list is empty
    if not data:
        raise ValueError("Data list is empty")

    # Check if the specified column is valid
    if column not in data.columns:
        raise KeyError(f"Invalid column: {column}")

    # Validate numeric values for steps, calories burned, and distance walked
    if column in ['steps', 'calories_burned', 'distance_walked']:
        if data[column].lt(0).any():
            raise ValueError(f"Negative values found in {column}")

    # Calculate the sum, mean, min, and max of the specified column
    column_stats = {
        'sum': data[column].sum(),
        'mean': data[column].mean(),
        'min': data[column].min(),
        'max': data[column].max()
    }

    # Plot the line chart
    fig, ax = plt.subplots()
    ax.plot(data['date'], data[column], marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel(column)
    ax.set_title(f'Line Chart of {column}')

    return (column_stats, ax)