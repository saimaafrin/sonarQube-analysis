
import numpy as np
import datetime

def task_func(arr):
    """
    Reverse the order of words separated by spaces in all strings of a numpy array.
    
    Parameters:
    arr (numpy.ndarray): A numpy array containing strings.
    
    Returns:
    numpy.ndarray: The numpy array with the strings reversed.
    """
    reversed_arr = np.array([' '.join(word.split()[::-1]) for word in arr])
    return reversed_arr