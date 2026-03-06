
import numpy as np
from scipy import stats

def task_func(L):
    """
    Calculate the mode of all elements in a nested list 'L'.

    Args:
        L (list): A nested list of integers.

    Returns:
        mode (int): The mode.
    """
    # Convert the nested list to a 1D numpy array
    arr = np.array(L)

    # Calculate the mode using the scipy.stats.mode function
    mode = stats.mode(arr)

    # Return the mode
    return mode