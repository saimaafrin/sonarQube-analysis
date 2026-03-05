import seaborn as sns
from random import sample
import pandas as pd
import matplotlib.pyplot as plt
def task_func(df, tuples, n_plots):
    """
    Removes rows from a dataframe based on values of multiple columns, and then creates n random pairs of two columns against each other to generate pairplots.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    tuples (list of tuples): A list of tuples where each tuple contains two column names and a value to filter by.
    n_plots (int): The number of pairplots to generate.
    
    Returns:
    tuple: A tuple containing:
        DataFrame: The modified DataFrame after removing specified rows.
        list of Axes: A list containing the generated pairplots.
    """
    # Remove rows based on the tuples
    for col1, col2, value in tuples:
        df = df[(df[col1] != value) | (df[col2] != value)]
    
    # Generate random pairs of columns for pairplots
    columns = df.columns.tolist()
    pairs = sample(list(zip(columns, columns)), n_plots)
    
    # Create pairplots
    pairplot_axes = []
    for pair in pairs:
        ax = sns.pairplot(df, x_vars=[pair[0]], y_vars=[pair[1]])
        pairplot_axes.append(ax)
    
    return df, pairplot_axes