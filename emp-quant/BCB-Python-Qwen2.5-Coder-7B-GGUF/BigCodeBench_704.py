
import pandas as pd
from itertools import combinations

# Constants
MIN_PERCENTAGE = 0.75

def task_func(data, cols, percentage):
    """
    Find all combinations of columns from a given DataFrame so that the absolute correlation between them is greater than a certain threshold.
    
    Parameters:
    data (pd.DataFrame): The input DataFrame.
    cols (list): A list of column names to consider for correlation.
    percentage (float): The minimum percentage correlation threshold.
    
    Returns:
    corr_combinations (list): A list of tuples where each tuple contains two column names.
    """
    corr_combinations = []
    # Calculate the correlation matrix for the specified columns
    corr_matrix = data[cols].corr()
    
    # Iterate over all combinations of columns
    for col1, col2 in combinations(cols, 2):
        # Check if the absolute correlation is greater than the threshold
        if abs(corr_matrix.loc[col1, col2]) > percentage:
            corr_combinations.append((col1, col2))
    
    return corr_combinations

    # Call the function
    result = task_func(data, cols, percentage)
    print(result)