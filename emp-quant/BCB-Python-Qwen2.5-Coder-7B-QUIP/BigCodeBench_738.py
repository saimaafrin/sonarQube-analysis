
import numpy as np
from scipy.stats import iqr

def task_func(L):
    # Flatten the nested list into a 1D array
    flattened = np.array(L).flatten()
    
    # Calculate the interquartile range
    iqr_value = iqr(flattened)
    
    return iqr_value