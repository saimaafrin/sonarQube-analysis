import pandas as pd
from itertools import combinations
def task_func(data, cols, percentage):
    """
    Find all combinations of columns from a given DataFrame so that the absolute correlation between them is greater than a certain threshold.
    :param data: A pandas DataFrame
    :param cols: A list of column names
    :param percentage: The minimum percentage of correlation required
    :return: A list of tuples where each tuple contains two column names
    """
    corr_combinations = []
    for col1, col2 in combinations(cols, 2):
        corr = data[col1].corr(data[col2])
        if abs(corr) > percentage:
            corr_combinations.append((col1, col2))
    return corr_combinations
data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
cols = ['A', 'B', 'C']