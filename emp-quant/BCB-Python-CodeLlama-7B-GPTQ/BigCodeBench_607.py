import pandas as pd
import matplotlib.pyplot as plt
from random import sample
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    """
    Remove rows from a dataframe based on column values and generate random scatter plots.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    tuples (list): A list of tuples containing column names and values to filter on.
    n_plots (int): The number of scatter plots to generate.

    Returns:
    pd.DataFrame: The DataFrame after removal of specified rows.
    list: A list containing matplotlib Axes objects of the generated plots.
    """
    # Remove rows from the DataFrame based on the specified column values
    filtered_df = df.copy()
    for col, val in tuples:
        filtered_df = filtered_df[filtered_df[col] != val]

    # Generate random scatter plots
    plots = []
    for i in range(n_plots):
        x = sample(filtered_df[COLUMNS[0]], 100)
        y = sample(filtered_df[COLUMNS[1]], 100)
        ax = plt.scatter(x, y)
        plots.append(ax)

    return filtered_df, plots
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'C': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'D': [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    'E': [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
})
tuples = [('A', 1)]
n_plots = 2