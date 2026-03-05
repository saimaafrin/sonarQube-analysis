
import numpy as np
import datetime

def task_func(arr):
    # Reverse the order of words separated by ". " in all strings of the numpy array
    arr_reversed = np.array([word.split(". ")[::-1] for word in arr])
    return arr_reversed