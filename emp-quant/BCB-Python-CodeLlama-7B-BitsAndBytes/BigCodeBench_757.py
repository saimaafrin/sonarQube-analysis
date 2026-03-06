
import numpy as np
import datetime

def task_func(arr):
    # Create a new array with the reversed strings
    new_arr = np.array([s[::-1] for s in arr])
    return new_arr