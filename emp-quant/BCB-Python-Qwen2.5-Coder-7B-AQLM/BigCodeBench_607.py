
import pandas as pd
import matplotlib.pyplot as plt
from random import sample
# Constants for column names to use in plots
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    """
    Removes rows from a dataframe based on column values and generates random scatter plots.
    
    Parameters:
    - df: pd.DataFrame - The input dataframe.
    - tuples: list - A list of tuples where each tuple contains column names and values to filter by.
    - n_plots: int - The number of scatter plots to generate.
    
    Returns:
    - pd.DataFrame: The DataFrame after removal of specified rows.
    - list: A list containing matplotlib Axes objects of the generated plots.
    """
    # Remove rows based on the tuples
    for col, value in tuples:
        df = df[df[col] != value]
    
    # Generate random scatter plots
    fig, axes = plt.subplots(n_plots, 1, figsize=(10, 15))
    axes = axes if n_plots > 1 else [axes]
    
    for ax in axes:
        cols = sample(COLUMNS, 2)
        ax.scatter(df[cols[0]], df[cols[1]])
        ax.set_xlabel(cols[0])
        ax.set_ylabel(cols[1])
        ax.set_title(f'Scatter plot of {cols[0]} vs {cols[1]}')
    
    plt.tight_layout()
    plt.show()
    
    return df, axes