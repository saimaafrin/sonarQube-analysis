
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(data, column="c"):
    """
    Removes a column from a data dictionary if it exists, and then plots the remaining data if it contains numeric data.
    
    Parameters:
    data (dict): A dictionary where keys are column names and values are lists of data.
    column (str): The name of the column to remove. Defaults to "c".
    
    Returns:
    df (pd.DataFrame): The modified DataFrame after removing the specified column.
    ax (matplotlib.axes._axes.Axes or None): The plot of the modified DataFrame if there's numeric data to plot, otherwise None.
    """
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Check if the column exists and remove it
    if column in df.columns:
        df = df.drop(columns=[column])
    
    # Check if the DataFrame contains numeric data
    if df.select_dtypes(include=[np.number]).shape[1] > 0:
        # Plot the remaining data
        ax = df.plot(kind='bar')
    else:
        ax = None
    
    return df, ax