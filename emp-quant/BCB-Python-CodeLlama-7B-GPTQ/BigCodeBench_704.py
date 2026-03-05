import pandas as pd
from itertools import combinations
def task_func(data, cols, percentage):
    """
    Find all combinations of columns from a given DataFrame so that the absolute correlation between them is greater than a certain threshold.
    """
    corr_combinations = []
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            if abs(data[cols[i]].corr(data[cols[j]])) > percentage:
                corr_combinations.append((cols[i], cols[j]))
    return corr_combinations
data = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10],
    'C': [11, 12, 13, 14, 15],
    'D': [16, 17, 18, 19, 20],
    'E': [21, 22, 23, 24, 25],
})