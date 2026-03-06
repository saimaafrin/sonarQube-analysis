
import pandas as pd
import matplotlib.pyplot as plt
from random import sample

# Constants for column names to use in plots
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    """
    Removes rows from a dataframe based on column values and generates random scatter plots.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    tuples (list): A list of tuples where each tuple contains two elements (column_name, value).
                   Rows where any of these conditions are met will be removed.
    n_plots (int): The number of scatter plots to generate.

    Returns:
    pd.DataFrame: The DataFrame after removal of specified rows.
    list: A list containing matplotlib Axes objects of the generated plots.
    """
    # Remove rows based on the given tuples
    mask = True
    for col, val in tuples:
        if col in df.columns:
            mask &= ~df[col].eq(val)
    cleaned_df = df[mask]

    # Generate random scatter plots
    fig, axes = plt.subplots(nrows=n_plots, ncols=1, figsize=(8, 6 * n_plots))
    if not isinstance(axes, np.ndarray):
        axes = [axes]  # Ensure axes is always a list

    for ax in axes:
        plot_cols = sample(COLUMNS, 2)
        ax.scatter(cleaned_df[plot_cols[0]], cleaned_df[plot_cols[1]])
        ax.set_xlabel(plot_cols[0])
        ax.set_ylabel(plot_cols[1])

    return cleaned_df, axes.tolist()