
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Check if the quantity sold or total sales is negative
    if np.any(data[column] < 0):
        raise ValueError("Negative value in column")

    # Calculate the sum, mean, minimum, and maximum of the column
    sum_ = data[column].sum()
    mean_ = data[column].mean()
    min_ = data[column].min()
    max_ = data[column].max()

    # Create a dictionary with the calculated values
    result = {
        "sum": sum_,
        "mean": mean_,
        "min": min_,
        "max": max_
    }

    # Plot the bar chart
    fig, ax = plt.subplots()
    ax.bar(data[column].index, data[column], label=column)
    ax.set_xlabel("Product")
    ax.set_ylabel("Quantity Sold")
    ax.set_title("Bar Chart of " + column)
    ax.legend()

    return result, fig