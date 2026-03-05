import numpy as np
import math
def task_func(L):
    """
    Calculate the median of all elements in a nested list 'L'.
    """
    # Check if the input is a list
    if not isinstance(L, list):
        raise ValueError("Input must be a list")

    # Flatten the list
    flat_list = [item for sublist in L for item in sublist]

    # Calculate the median
    median = np.median(flat_list)

    # Return the median
    return median
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]