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
    # Convert the numpy array to a list of strings
    str_list = arr.tolist()
    
    # Reverse the order of words in each string
    reversed_str_list = [' '.join(s.split()[::-1]) for s in str_list]
    
    # Convert the list back to a numpy array
    reversed_arr = np.array(reversed_str_list)
    
    return reversed_arr