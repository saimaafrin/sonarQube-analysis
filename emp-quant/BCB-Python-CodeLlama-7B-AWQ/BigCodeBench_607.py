import pandas as pd
import matplotlib.pyplot as plt
from random import sample
def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    """
    Remove rows from a dataframe based on column values and generate random scatter plots.
    :param df: The input dataframe.
    :param tuples: A list of tuples containing column names and values to remove.
    :param n_plots: The number of plots to generate.
    :return: A tuple containing the modified dataframe and a list of matplotlib Axes objects.
    """
    # Remove rows from the dataframe based on the specified column values
    for col, val in tuples:
        df = df[df[col] != val]

    # Generate random scatter plots
    plots = []
    for i in range(n_plots):
        x = sample(df['A'], 100)
        y = sample(df['B'], 100)
        ax = plt.scatter(x, y)
        plots.append(ax)

    return df, plots
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})
tuples = [('A', 3), ('B', 7)]
n_plots = 2