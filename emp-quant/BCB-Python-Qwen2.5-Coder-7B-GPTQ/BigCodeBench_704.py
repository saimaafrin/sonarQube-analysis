import pandas as pd
from itertools import combinations
def task_func(data, cols, percentage):
    """
    Find all combinations of columns from a given DataFrame so that the absolute correlation between them is greater than a certain threshold.
    
    Parameters:
    data (pd.DataFrame): The input DataFrame.
    cols (list): List of column names to consider for correlation.
    percentage (float): The minimum percentage of correlation to consider.
    
    Returns:
    corr_combinations (list): A list of tuples where each tuple contains two column names.
    """
    corr_combinations = []
    for col1, col2 in combinations(cols, 2):
        corr = data[col1].corr(data[col2])
        if abs(corr) > percentage:
            corr_combinations.append((col1, col2))
    return corr_combinations