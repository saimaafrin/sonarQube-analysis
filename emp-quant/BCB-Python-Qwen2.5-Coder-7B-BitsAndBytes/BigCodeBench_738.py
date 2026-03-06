
import numpy as np
from scipy.stats import iqr

def task_func(L):
    # Flatten the nested list into a 1D array
    flattened_list = [item for sublist in L for item in sublist]
    
    # Calculate the interquartile range using the iqr function from scipy.stats
    iqr_value = iqr(flattened_list)
    
    return iqr_value