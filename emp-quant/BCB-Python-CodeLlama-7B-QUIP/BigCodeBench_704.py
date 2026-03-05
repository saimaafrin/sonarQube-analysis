
import pandas as pd
from itertools import combinations

# Constants
MIN_PERCENTAGE = 0.75

def task_func(data, cols, percentage):
    # Initialize the list of combinations
    corr_combinations = []

    # Loop through all possible combinations of columns
    for c1, c2 in combinations(cols, 2):
        # Calculate the absolute correlation between the two columns
        corr = abs(data[c1].corr(data[c2]))

        # Check if the correlation is greater than the minimum percentage
        if corr > MIN_PERCENTAGE:
            # Add the combination to the list of combinations
            corr_combinations.append((c1, c2))

    return corr_combinations