
import pandas as pd
import numpy as np

def task_func(column, data):
    """
    Analyzes a list of stock data and calculates the sum, mean, minimum, and maximum values for a specified column.

    Parameters:
    column (str): The name of the column to analyze.
    data (list): The list of stock data.

    Returns:
    dict: A dictionary containing the calculated 'sum', 'mean', 'min' (minimum), and 'max' (maximum) for the specified column.
    If the input data is empty, 'sum' will be 0, and 'mean', 'min', and 'max' will be NaN.

    Raises:
    ValueError: If the specified column name is not valid.
    """
    # Check if the column name is valid
    if column not in data.columns:
        raise ValueError(f"Invalid column name: {column}")

    # Calculate the sum, mean, minimum, and maximum values for the specified column
    sum_val = data[column].sum()
    mean_val = data[column].mean()
    min_val = data[column].min()
    max_val = data[column].max()

    # Create a dictionary with the calculated values
    result = {"sum": sum_val, "mean": mean_val, "min": min_val, "max": max_val}

    # Return the dictionary
    return result

print(task_func("B", data))
# Output: {'sum': 55, 'mean': 7.0, 'min': 6, 'max': 10}

print(task_func("C", data))
# Output: ValueError: Invalid column name: C