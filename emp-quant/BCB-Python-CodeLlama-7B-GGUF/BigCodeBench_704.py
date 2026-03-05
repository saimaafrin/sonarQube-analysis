
import pandas as pd
from itertools import combinations

# Constants
MIN_PERCENTAGE = 0.75

def task_func(data, cols, percentage):
    """
    Find all combinations of columns from a given DataFrame so that the absolute correlation between them is greater than a certain threshold.

    Args:
        data (pd.DataFrame): The DataFrame to search for correlated columns.
        cols (list): A list of column names to consider for correlation.
        percentage (float): The minimum percentage of correlation required for a column pair to be considered.

    Returns:
        corr_combinations (list): A list of tuples where each tuple contains two column names.
    """
    corr_combinations = []
    for col1, col2 in combinations(cols, 2):
        corr = data[col1].corr(data[col2])
        if abs(corr) > percentage:
            corr_combinations.append((col1, col2))
    return corr_combinations

corr_combinations = task_func(data, cols, percentage)
print(corr_combinations)