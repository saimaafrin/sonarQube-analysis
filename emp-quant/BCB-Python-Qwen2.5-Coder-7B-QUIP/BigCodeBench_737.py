
import numpy as np
import math

def task_func(L):
    # Flatten the nested list into a 1D list
    flattened = [item for sublist in L for item in sublist]
    
    # Calculate the median
    median = np.median(flattened)
    
    return median