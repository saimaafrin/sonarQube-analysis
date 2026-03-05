import numpy as np
import random
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
def task_func(l=None):
    """
    Create a numeric array from a list "l" and move the first 3 elements to the end of the array.
    """
    if l is None:
        l = ELEMENTS
    arr = np.array(l)
    arr = np.roll(arr, 3)
    return arr