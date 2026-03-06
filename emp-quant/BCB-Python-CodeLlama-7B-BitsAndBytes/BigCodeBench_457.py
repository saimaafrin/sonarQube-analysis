
import pandas as pd
import numpy as np

def task_func(L):
    # Check if input is a list of lists of integers
    if not all(isinstance(sublist, list) and all(isinstance(item, int) for item in sublist) for sublist in L):
        raise TypeError("Input must be a list of lists of integers")

    # Convert nested list to a 1D numpy array
    arr = np.array(L)

    # Flatten the array and remove any empty sublists
    arr = arr.flatten()
    arr = arr[arr != []]

    # Create a histogram of the flattened array
    ax = pd.Series(arr).hist(rwidth=0.8)

    return ax