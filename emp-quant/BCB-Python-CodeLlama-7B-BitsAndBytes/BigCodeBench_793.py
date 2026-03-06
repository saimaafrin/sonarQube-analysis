
import numpy as np
import random
# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
def task_func(l=None):
    # Create a numpy array from the list
    arr = np.array(l)
    # Move the first three elements to the end of the array
    arr = np.roll(arr, 3)
    return arr