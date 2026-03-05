import pandas as pd
import matplotlib.pyplot as plt
from random import sample
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    """
    Remove rows from a dataframe based on column values and generate random scatter plots.

    Args:
        df (pd.DataFrame): The input DataFrame.
        tuples (list): A list of tuples containing column names and values to remove.
        n_plots (int): The number of plots to generate.

    Returns:
        pd.DataFrame: The DataFrame after removal of specified rows.
        list: A list containing matplotlib Axes objects of the generated plots.
    """
    # Remove rows from the DataFrame based on the specified column values
    df = df.drop(df[df[tuples[0][0]] == tuples[0][1]].index)
    for i in range(1, len(tuples)):
        df = df.drop(df[df[tuples[i][0]] == tuples[i][1]].index)

    # Generate random scatter plots
    plots = []
    for i in range(n_plots):
        x = sample(df[COLUMNS[0]], 100)
        y = sample(df[COLUMNS[1]], 100)
        ax = plt.scatter(x, y)
        plots.append(ax)

    return df, plots
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20], 'E': [21, 22, 23, 24, 25]})
tuples = [('A', 3), ('B', 7), ('C', 13)]
n_plots = 3