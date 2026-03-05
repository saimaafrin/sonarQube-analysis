import numpy as np
from scipy import stats
def task_func(L):
    """
    Calculate the mode of all elements in a nested list 'L'.
    """
    # Calculate the mode of each sublist
    modes = [stats.mode(sublist) for sublist in L]

    # Find the most common mode
    mode = max(modes, key=modes.count)

    return mode
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]