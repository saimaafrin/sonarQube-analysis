
import numpy as np
import math

def task_func(L):
    # Flatten the nested list into a single list
    flattened_list = [item for sublist in L for item in sublist]
    
    # Convert the list to a numpy array
    arr = np.array(flattened_list)
    
    # Calculate the median using numpy's median function
    median_value = np.median(arr)
    
    return median_value