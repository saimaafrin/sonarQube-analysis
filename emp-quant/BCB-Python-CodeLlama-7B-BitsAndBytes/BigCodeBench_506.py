
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Calculate the sum, mean, minimum, and maximum values of the specified column
    sum_val = data[column].sum()
    mean_val = data[column].mean()
    min_val = data[column].min()
    max_val = data[column].max()

    # Generate a histogram plot of the data in the specified column
    fig, ax = plt.subplots()
    ax.hist(data[column], bins=20)
    ax.set_title(f"Histogram of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")
    ax.set_xticks([])
    ax.set_yticks([])
    plt.tight_layout()

    # Create a dictionary with the results
    result = {
        'sum': sum_val,
        'mean': mean_val,
        'min': min_val,
        'max': max_val,
        'plot': fig
    }

    return result

result = task_func('temperature', data)
print(result)