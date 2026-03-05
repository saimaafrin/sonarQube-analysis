
import pandas as pd
import numpy as np

def task_func(column, data):
    # Check if the column name is valid
    if column not in data.columns:
        raise ValueError("Invalid column name")

    # Calculate the sum, mean, minimum, and maximum values for the specified column
    sum_val = data[column].sum()
    mean_val = data[column].mean()
    min_val = data[column].min()
    max_val = data[column].max()

    # Create a dictionary with the calculated values
    result = {
        "sum": sum_val,
        "mean": mean_val,
        "min": min_val,
        "max": max_val
    }

    return result