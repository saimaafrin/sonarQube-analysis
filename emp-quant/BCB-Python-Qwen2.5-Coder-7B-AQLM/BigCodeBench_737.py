
import numpy as np
import math

def task_func(L):
    # Flatten the nested list
    flattened_list = [item for sublist in L for item in sublist]
    
    # Convert the flattened list to a numpy array
    array = np.array(flattened_list)
    
    # Calculate the median
    median = np.median(array)
    
    return median