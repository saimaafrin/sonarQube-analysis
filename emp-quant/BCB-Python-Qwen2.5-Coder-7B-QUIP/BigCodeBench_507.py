
import pandas as pd
import numpy as np

def task_func(column, data):
    # Check if the column exists in the data
    if column not in data.columns:
        raise ValueError("Invalid column name")

    # Calculate the sum, mean, minimum, and maximum values for the specified column
    sum_value = data[column].sum()
    mean_value = data[column].mean()
    min_value = data[column].min()
    max_value = data[column].max()

    # Return the results as a dictionary
    return {
        'sum': sum_value,
        'mean': mean_value,
        'min': min_value,
        'max': max_value
    }