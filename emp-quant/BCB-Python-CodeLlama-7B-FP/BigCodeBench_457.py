import pandas as pd
import numpy as np
def task_func(L):
    """
    Draw a histogram of all elements in a nested list 'L' and return the Axes object of the plot.
    The function first uses Numpy to handle array operations, checking for correct input type while ignoring empty sublists.
    It then plots the histogram using pandas, assigning each unique value its own bin and plotting the histogram with rwidth 0.8.
    The function should raise the exception for:
        - If the input is not a list of list of integers, a TypeError is raised.
    The function should output with:
        - ax (matplotlib.axes._axes.Axes): The Axes object of the histogram plot.
    """
    # Check input type
    if not isinstance(L, list):
        raise TypeError("Input must be a list of lists of integers.")

    # Convert nested list to 1D array
    L = np.array(L)

    # Flatten nested list
    L = L.flatten()

    # Create histogram
    ax = pd.DataFrame(L).hist(bins=np.unique(L), rwidth=0.8)

    return ax
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]