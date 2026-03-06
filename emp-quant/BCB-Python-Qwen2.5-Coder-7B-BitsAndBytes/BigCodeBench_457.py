
import pandas as pd
import numpy as np

def task_func(L):
    """
    Draws a histogram of all elements in a nested list 'L' and returns the Axes object of the plot.

    Parameters:
    L (list of list of int): A nested list containing integer values.

    Returns:
    ax (matplotlib.axes._axes.Axes): The Axes object of the histogram plot.
    """

    # Check if the input is a list of lists of integers
    if not isinstance(L, list) or not all(isinstance(sublist, list) for sublist in L) or not all(isinstance(item, int) for sublist in L for item in sublist):
        raise TypeError("Input must be a list of lists of integers")

    # Flatten the nested list and filter out empty sublists
    flat_list = [item for sublist in L for item in sublist if item != []]

    # Convert the flattened list to a pandas Series
    series = pd.Series(flat_list)

    # Plot the histogram
    ax = series.plot(kind='hist', bins=range(min(series), max(series) + 2), rwidth=0.8)

    return ax