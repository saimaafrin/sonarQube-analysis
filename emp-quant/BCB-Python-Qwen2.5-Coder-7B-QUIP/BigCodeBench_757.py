
import numpy as np
import datetime

def task_func(arr):
    # Convert the numpy array to a list of strings
    arr_list = arr.tolist()
    
    # Reverse the order of words in each string
    reversed_list = [s[::-1] for s in arr_list]
    
    # Convert the list back to a numpy array
    reversed_arr = np.array(reversed_list)
    
    return reversed_arr