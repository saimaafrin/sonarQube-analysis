
import numpy as np

def task_func(arr):
    # Reverse the order of words separated by "." in all strings of a numpy array
    return np.char.split(arr, ".").swapaxes(0, 1)[::-1].reshape(arr.shape)