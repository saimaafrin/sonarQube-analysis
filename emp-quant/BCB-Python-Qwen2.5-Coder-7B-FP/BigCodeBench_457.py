import pandas as pd
import numpy as np
def task_func(L):
    """
    Draw a histogram of all elements in a nested list 'L' and return the Axes object of the plot.
    
    Parameters:
    L (list of list of int): A nested list of integers.
    
    Returns:
    ax (matplotlib.axes._axes.Axes): The Axes object of the histogram plot.
    
    Raises:
    TypeError: If the input is not a list of list of integers.
    """
    # Check if L is a list of lists
    if not all(isinstance(sublist, list) for sublist in L):
        raise TypeError("Input must be a list of lists.")
    
    # Flatten the list and filter out non-integer values
    flat_list = [item for sublist in L for item in sublist if isinstance(item, int)]
    
    # Check if the flattened list is empty
    if not flat_list:
        raise ValueError("The list contains no integers.")
    
    # Create a pandas Series from the flattened list
    series = pd.Series(flat_list)
    
    # Plot the histogram
    ax = series.plot(kind='hist', rwidth=0.8, bins='auto')
    
    return ax