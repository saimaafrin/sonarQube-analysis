
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Check if the data list is empty
    if len(data) == 0:
        # Set the mean, min, and max values to np.nan
        mean = np.nan
        min = np.inf
        max = -np.inf
    else:
        # Calculate the sum, mean, min, and max values of the specified column
        sum = data[column].sum()
        mean = data[column].mean()
        min = data[column].min()
        max = data[column].max()

    # Generate a histogram plot of the specified column
    fig, ax = plt.subplots()
    ax.hist(data[column], bins=50)
    ax.set_title(f"Histogram of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")
    plt.show()

    # Return a dictionary containing the results
    return {
        "sum": sum,
        "mean": mean,
        "min": min,
        "max": max,
        "plot": fig
    }