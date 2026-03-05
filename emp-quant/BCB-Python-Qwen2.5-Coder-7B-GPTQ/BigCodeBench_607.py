import pandas as pd
import matplotlib.pyplot as plt
from random import sample
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    """
    Removes rows from a dataframe based on column values and generates random scatter plots.
    
    Parameters:
    - df: pd.DataFrame - The input DataFrame.
    - tuples: list - A list of tuples, each containing column names and values to filter by.
    - n_plots: int - The number of scatter plots to generate.
    
    Returns:
    - pd.DataFrame: The DataFrame after removal of specified rows.
    - list: A list containing matplotlib Axes objects of the generated plots.
    """
    # Remove rows based on the specified tuples
    for col, value in tuples:
        df = df[df[col] != value]
    
    # Generate random scatter plots
    fig, axes = plt.subplots(n_plots, 1, figsize=(8, 2 * n_plots))
    if n_plots == 1:
        axes = [axes]  # Ensure axes is a list for consistent indexing
    
    for ax in axes:
        # Select two random columns for plotting
        cols = sample(COLUMNS, 2)
        ax.scatter(df[cols[0]], df[cols[1]])
        ax.set_xlabel(cols[0])
        ax.set_ylabel(cols[1])
    
    plt.tight_layout()
    plt.show()
    
    return df, axes