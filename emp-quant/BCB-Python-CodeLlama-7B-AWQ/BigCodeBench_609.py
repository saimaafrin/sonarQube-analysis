import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from random import sample
def task_func(df, tuples, n_plots):
    """
    Removes rows from a DataFrame based on a list of tuples, each representing row values to match and remove. Generates up to 'n_plots' scatter plots for random combinations of two columns from the remaining DataFrame.
    The function should output with:
        pd.DataFrame: The DataFrame after specified rows have been removed.
        list: A list of tuples, each containing a pair of column names used for the plot and the corresponding plot object.
    """
    # Remove rows from DataFrame based on tuples
    for tuple in tuples:
        df = df[~(df[tuple[0]] == tuple[1])]

    # Generate random combinations of two columns for scatter plots
    columns = list(df.columns)
    column_pairs = combinations(columns, 2)
    random_pairs = sample(column_pairs, n_plots)

    # Create scatter plots
    plot_list = []
    for pair in random_pairs:
        x = df[pair[0]]
        y = df[pair[1]]
        plot = plt.scatter(x, y)
        plot_list.append((pair, plot))

    return df, plot_list
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': [3, 6, 9, 12, 15]})
tuples = [(1, 2), (3, 4)]
n_plots = 2