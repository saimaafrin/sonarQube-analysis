from itertools import combinations
from random import sample
import pandas as pd
import matplotlib.pyplot as plt
def task_func(df, tuples, n_plots):
    """
    Removes rows from a DataFrame based on a list of tuples, each representing row values to match and remove.
    Generates up to 'n_plots' scatter plots for random combinations of two columns from the remaining DataFrame.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - tuples (list of tuples): Each tuple contains row values to match and remove.
    - n_plots (int): The maximum number of scatter plots to generate.
    
    Returns:
    - pd.DataFrame: The DataFrame after specified rows have been removed.
    - list: A list of tuples, each containing a pair of column names used for the plot and the corresponding plot object.
    """
    # Remove rows based on the list of tuples
    df_filtered = df[~df.isin(tuples).all(axis=1)]
    
    # Generate scatter plots for random combinations of two columns
    plots = []
    for _ in range(min(n_plots, len(list(combinations(df_filtered.columns, 2))))):
        cols = sample(list(combinations(df_filtered.columns, 2)), 1)[0]
        plot = df_filtered.plot.scatter(x=cols[0], y=cols[1])
        plots.append((cols, plot))
    
    return df_filtered, plots