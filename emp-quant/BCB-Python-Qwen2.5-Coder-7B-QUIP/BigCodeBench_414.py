
import pandas as pd
import numpy as np
def task_func(data, column="c"):
    """
    Remove a column from a data dictionary if it exists, and then plot the remaining data if it contains numeric data.
    
    Parameters:
    data (dict): A dictionary representing the data.
    column (str): The column name to remove. Defaults to "c".
    
    Returns:
    df (pd.DataFrame): The modified DataFrame after removing the specified column.
    ax (matplotlib.axes._axes.Axes or None): The plot of the modified DataFrame if there's
    numeric data to plot, otherwise None.
    """
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Check if the column exists and remove it
    if column in df.columns:
        df = df.drop(columns=[column])
    
    # Check if there is numeric data to plot
    if df.dtypes[0] == 'object':
        ax = None
    else:
        ax = df.plot()
    
    return df, ax