
import pandas as pd
from itertools import combinations
# Constants
MIN_PERCENTAGE = 0.75

def task_func(data, cols, percentage):
    corr_combinations = []
    for col1, col2 in combinations(cols, 2):
        corr = abs(data[col1].corr(data[col2]))
        if corr > percentage:
            corr_combinations.append((col1, col2))
    return corr_combinations