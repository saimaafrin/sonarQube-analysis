import numpy as np
import math
def task_func(L):
    """
    Calculate the median of all elements in a nested list 'L'.
    """
    # Convert the nested list to a 1D numpy array
    arr = np.array(L).flatten()

    # Calculate the median
    median = np.median(arr)

    # Return the median
    return median
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]