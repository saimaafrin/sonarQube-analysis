
import numpy as np
import random
# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
def task_func(l=None):
    arr = np.array(l)
    arr = np.roll(arr, 3)
    return arr