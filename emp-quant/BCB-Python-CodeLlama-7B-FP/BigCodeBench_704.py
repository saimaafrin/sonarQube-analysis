import pandas as pd
from itertools import combinations
def task_func(data, cols, percentage):
    """
    Find all combinations of columns from a given DataFrame so that the absolute correlation between them is greater than a certain threshold.
    :param data: A pandas DataFrame
    :param cols: A list of column names
    :param percentage: The minimum percentage of correlation between columns
    :return: A list of tuples where each tuple contains two column names
    """
    corr_combinations = []
    for col1, col2 in combinations(cols, 2):
        corr = data[col1].corr(data[col2])
        if abs(corr) > percentage:
            corr_combinations.append((col1, col2))
    return corr_combinations
data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': [3, 6, 9, 12, 15]})
cols = ['A', 'B', 'C']