import numpy as np
import random
def task_func(l=None):
    """
    Create a numeric array from a list "l" and move the first 3 elements to the end of the array.
    """
    # Check if the input list is valid
    if l is None:
        raise ValueError("Input list is None")
    # Create a numpy array from the input list
    arr = np.array(l)
    # Move the first 3 elements to the end of the array
    arr = np.roll(arr, 3)
    return arr