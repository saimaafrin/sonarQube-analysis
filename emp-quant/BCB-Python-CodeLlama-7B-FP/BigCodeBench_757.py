import numpy as np
import datetime
def task_func(arr):
    """
    Reverse the order of words separated by "." in all strings of a numpy array.
    """
    # Create a new array with the reversed strings
    new_arr = np.array([s[::-1] for s in arr])
    return new_arr
arr = np.array(['hello.world', 'goodbye.world'])