
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, bins=20):
    """
    Draws a histogram of the last column of the DataFrame and returns the plot.

    Parameters:
    df (pd.DataFrame): Input DataFrame.
    bins (int): Number of bins to use in the histogram.

    Returns:
    Axes: A Matplotlib Axes object representing the histogram of the last column.

    Raises:
    ValueError: If the input is not a DataFrame, or if the DataFrame is empty.
    """
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame.")
    
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame cannot be empty.")
    
    # Get the last column of the DataFrame
    last_column = df.iloc[:, -1]
    
    # Create the histogram
    ax = last_column.hist(bins=bins)
    
    # Set the title of the histogram
    ax.set_title(f'Histogram of {last_column.name}')
    
    # Set the labels for the axes
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Return the Axes object
    return ax