import pandas as pd
import matplotlib.pyplot as plt
from random import sample
COLUMNS = ['A', 'B', 'C', 'D', 'E']
def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    """
    Removes rows from a dataframe based on column values and generates random scatter plots.
    
    Parameters:
    - df: pd.DataFrame - The input DataFrame.
    - tuples: list - A list of tuples, each containing two values (column name, value) to filter rows.
    - n_plots: int - The number of scatter plots to generate.
    
    Returns:
    - pd.DataFrame: The DataFrame after removal of specified rows.
    - list: A list containing matplotlib Axes objects of the generated plots.
    """
    # Remove rows based on the specified tuples
    mask = ~df.isin(dict(tuples)).any(axis=1)
    df_filtered = df[mask]
    
    # Generate random scatter plots
    fig, axes = plt.subplots(n_plots, figsize=(10, 10))
    axes = axes.flatten() if n_plots > 1 else [axes]
    
    for ax in axes:
        # Randomly select two columns for the scatter plot
        cols = sample(COLUMNS, 2)
        ax.scatter(df_filtered[cols[0]], df_filtered[cols[1]])
        ax.set_xlabel(cols[0])
        ax.set_ylabel(cols[1])
    
    return df_filtered, axes.tolist()