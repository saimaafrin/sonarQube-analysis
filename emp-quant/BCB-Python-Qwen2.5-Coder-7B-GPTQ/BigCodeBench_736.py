import numpy as np
from scipy import stats
def task_func(L):
    # Flatten the nested list into a 1D array
    flattened_list = [item for sublist in L for item in sublist]
    
    # Calculate the mode using scipy's mode function
    mode_result = stats.mode(flattened_list)
    
    # Return the mode as an integer
    return mode_result.mode[0]