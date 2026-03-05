import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from random import sample
def task_func(df, tuples, n_plots):
    """
    Removes rows from a DataFrame based on a list of tuples, each representing row values to match and remove.
    Generates up to 'n_plots' scatter plots for random combinations of two columns from the remaining DataFrame.
    Returns a tuple containing the modified DataFrame and a list of tuples, each containing a pair of column names used for the plot and the corresponding plot object.
    """
    # Remove rows from the DataFrame based on the tuples
    for tuple in tuples:
        df = df[~df[tuple[0]].isin(tuple[1])]

    # Generate random combinations of two columns for the scatter plots
    columns = df.columns
    combinations = combinations(columns, 2)
    random_combinations = sample(combinations, n_plots)

    # Create scatter plots for each random combination
    plots = []
    for combination in random_combinations:
        x = df[combination[0]]
        y = df[combination[1]]
        plot = plt.scatter(x, y)
        plots.append((combination, plot))

    return df, plots
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15]})
tuples = [(['A', 'B'], [1, 2]), (['A', 'C'], [11, 12])]
n_plots = 2