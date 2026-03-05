import numpy as np
from scipy.stats import iqr
def task_func(L):
    """
    Calculate the interquartile range of all elements in a nested list 'L'.
    """
    # Calculate the interquartile range
    iqr_value = iqr(L)

    # Return the interquartile range
    return iqr_value
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]