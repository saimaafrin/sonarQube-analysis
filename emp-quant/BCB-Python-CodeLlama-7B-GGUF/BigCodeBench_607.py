
import pandas as pd
import matplotlib.pyplot as plt
from random import sample

# Constants for column names to use in plots
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    """
    Remove rows from a dataframe based on column values and generate random scatter plots.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    tuples (list): A list of tuples containing column names and values to remove.
    n_plots (int): The number of scatter plots to generate.

    Returns:
    pd.DataFrame: The DataFrame after removal of specified rows.
    list: A list containing matplotlib Axes objects of the generated plots.
    """
    # Remove rows based on column values
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

df, plots = task_func(df, tuples, n_plots)

# Show plots
plt.show()