import pandas as pd
import numpy as np
def task_func(L):
    """
    Draw a histogram of all elements in a nested list 'L' and return the Axes object of the plot.
    The function first uses Numpy to handle array operations, checking for correct input type while ignoring empty sublists.
    It then plots the histogram using pandas, assigning each unique value its own bin and plotting the histogram with rwidth 0.8.
    The function should raise the exception for:
        If the input is not a list of list of integers, a TypeError is raised.
    The function should output with:
        ax (matplotlib.axes._axes.Axes): The Axes object of the histogram plot.
    """
    # Check input type
    if not isinstance(L, list):
        raise TypeError("Input must be a list of lists of integers")

    # Convert list of lists to a 1D numpy array
    L = np.array(L)

    # Flatten the array and remove empty sublists
    L = L.flatten()
    L = L[L != []]

    # Create a pandas Series from the flattened array
    s = pd.Series(L)

    # Plot the histogram
    ax = s.plot.hist(rwidth=0.8)

    return ax
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]