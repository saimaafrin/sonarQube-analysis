import numpy as np
from scipy.stats import iqr
def task_func(L):
    """
    Calculate the interquartile range of all elements in a nested list 'L'.
    """
    # Check if the input is a list
    if not isinstance(L, list):
        raise ValueError("Input must be a list")

    # Check if the list is empty
    if len(L) == 0:
        raise ValueError("Input list is empty")

    # Flatten the list
    flattened_list = [item for sublist in L for item in sublist]

    # Calculate the interquartile range
    iqr_value = iqr(flattened_list)

    return iqr_value
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]