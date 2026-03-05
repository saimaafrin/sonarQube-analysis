import pandas as pd
import matplotlib.pyplot as plt
def task_func(d, keys=['x', 'y', 'z']):
    """
    Plots values from a list of dictionaries based on specified keys and returns the plot as a Matplotlib Axes object.

    Parameters:
    d (list of dict): List of dictionaries containing data.
    keys (list of str): List of keys to plot. Default is ['x', 'y', 'z'].

    Returns:
    matplotlib.axes._axes.Axes: The plot showing the values of specified keys from the input list of dictionaries.
    """
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(d)
    
    # Plot the specified keys
    ax = df[keys].plot()
    
    return ax
data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}, {'x': 7, 'y': 8, 'z': 9}]