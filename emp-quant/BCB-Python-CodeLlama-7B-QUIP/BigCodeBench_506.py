
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Check if the data is empty
    if len(data) == 0:
        return {
            'sum': np.nan,
            'mean': np.nan,
            'min': np.inf,
            'max': -np.inf
        }

    # Calculate the sum, mean, minimum, and maximum values
    sum_val = data[column].sum()
    mean_val = data[column].mean()
    min_val = data[column].min()
    max_val = data[column].max()

    # Generate a histogram plot
    fig, ax = plt.subplots()
    ax.hist(data[column], bins=50)
    ax.set_xlabel(f'{column}')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Histogram of {column}')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_xticks(np.arange(0, 101, 5))
    ax.set_yticks(np.arange(0, 101, 5))
    ax.grid(True)
    fig.tight_layout()

    # Return a dictionary containing the results
    return {
        'sum': sum_val,
        'mean': mean_val,
        'min': min_val,
        'max': max_val,
        'plot': fig
    }