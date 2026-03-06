
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Validate the column name
    if column not in data.columns:
        raise KeyError(f"Invalid column name: {column}")

    # Validate the data list
    if len(data) == 0:
        raise ValueError("Data list is empty")

    # Calculate the sum, mean, min, and max of the column
    sum_val = data[column].sum()
    mean_val = data[column].mean()
    min_val = data[column].min()
    max_val = data[column].max()

    # Validate the numeric values for steps, calories burned, and distance walked
    if any(data[column] < 0):
        raise ValueError("Negative value found in column")

    # Plot the line chart
    fig, ax = plt.subplots()
    ax.plot(data.index, data[column], label=f"Line Chart of {column}")
    ax.set_xlabel("Date")
    ax.set_ylabel(column)
    ax.set_title(f"Line Chart of {column}")
    ax.legend()

    return (dict(sum=sum_val, mean=mean_val, min=min_val, max=max_val), ax)

result = task_func("Steps", data)
print(result)