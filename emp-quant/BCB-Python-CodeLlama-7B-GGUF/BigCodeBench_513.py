
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Validate input
    if column not in data.columns:
        raise KeyError(f"Invalid column: {column}")
    if len(data) == 0:
        raise ValueError("Data list is empty")
    if data[column].isnull().any():
        raise ValueError("Numeric values for steps, calories burned, and distance walked cannot be null")
    if data[column].dtypes != np.float64:
        raise ValueError("Numeric values for steps, calories burned, and distance walked must be of type float64")
    if data[column].min() < 0:
        raise ValueError("Numeric values for steps, calories burned, and distance walked must be non-negative")

    # Calculate sum, mean, min, max of column
    sum_val = data[column].sum()
    mean_val = data[column].mean()
    min_val = data[column].min()
    max_val = data[column].max()

    # Plot line chart
    fig, ax = plt.subplots()
    ax.plot(data["Date"], data[column], label=f"Line Chart of {column}")
    ax.set_xlabel("Date")
    ax.set_ylabel(column)
    ax.set_title(f"Line Chart of {column}")
    ax.legend()

    # Return tuple of dict and Axes object
    return ({"sum": sum_val, "mean": mean_val, "min": min_val, "max": max_val}, ax)