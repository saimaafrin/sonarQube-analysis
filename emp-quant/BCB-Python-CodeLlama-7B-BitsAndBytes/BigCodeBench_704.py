
import pandas as pd
from itertools import combinations

# Constants
MIN_PERCENTAGE = 0.75

def task_func(data, cols, percentage):
    # Calculate the absolute correlation between each pair of columns
    correlations = data[cols].corr().abs()

    # Find the combinations of columns with a correlation greater than the threshold
    corr_combinations = []
    for col1, col2 in combinations(cols, 2):
        if correlations.loc[col1, col2] > percentage:
            corr_combinations.append((col1, col2))

    return corr_combinations

# Call the function
corr_combinations = task_func(data, cols, percentage)

print(corr_combinations)