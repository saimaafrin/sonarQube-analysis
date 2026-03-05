import pandas as pd
import numpy as np
def task_func(column, data):
    """
    Analyzes a list of stock data and calculates the sum, mean, minimum, and maximum values for a specified column.
    The function should raise the exception for: ValueError: If the specified column name is not valid.
    The function should output with:
        dict: A dictionary containing the calculated 'sum', 'mean', 'min' (minimum), and 'max' (maximum)
        for the specified column. If the input data is empty, 'sum' will be 0, and 'mean', 'min', and
        'max' will be NaN.
    """
    if column not in data.columns:
        raise ValueError(f"{column} is not a valid column name")

    # Calculate the sum, mean, minimum, and maximum values for the specified column
    sum_ = data[column].sum()
    mean = data[column].mean()
    min_ = data[column].min()
    max_ = data[column].max()

    # Create a dictionary with the calculated values
    result = {
        "sum": sum_,
        "mean": mean,
        "min": min_,
        "max": max_,
    }

    return result
data = pd.DataFrame({
    "A": [1, 2, 3, 4, 5],
    "B": [10, 20, 30, 40, 50],
})