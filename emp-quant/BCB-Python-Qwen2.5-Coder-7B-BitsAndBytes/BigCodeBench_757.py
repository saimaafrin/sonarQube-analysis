
import numpy as np
import datetime

def task_func(arr):
    """
    Reverse the order of words separated by spaces in all strings of a numpy array.

    Parameters:
    arr (numpy.ndarray): A numpy array containing string elements.

    Returns:
    numpy.ndarray: The numpy array with the strings reversed.
    """
    # Convert the numpy array to a list of strings
    str_list = arr.tolist()
    
    # Reverse each word in each string and create a new list
    reversed_str_list = [' '.join(word[::-1] for word in s.split()) for s in str_list]
    
    # Convert the list back to a numpy array
    result_arr = np.array(reversed_str_list)
    
    return result_arr