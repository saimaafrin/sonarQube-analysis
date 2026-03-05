import pandas as pd
import matplotlib.pyplot as plt
def task_func(df, bins=20):
    """
    Draws a histogram of the last column of the DataFrame and returns the plot.
    
    Parameters:
    - df: pandas DataFrame
    - bins: int, optional. Number of bins in the histogram. Default is 20.
    
    Returns:
    - Axes: A Matplotlib Axes object representing the histogram of the last column.
    
    Raises:
    - ValueError: If the input is not a DataFrame, or if the DataFrame is empty.
    """
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty.")
    
    # Get the last column of the DataFrame
    last_column = df.columns[-1]
    
    # Draw the histogram
    ax = df[last_column].hist(bins=bins)
    
    # Set the title, x-axis label, and y-axis label
    ax.set_title(f'Histogram of {last_column}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    return ax