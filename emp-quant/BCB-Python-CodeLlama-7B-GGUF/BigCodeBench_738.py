
import numpy as np
from scipy.stats import iqr

def task_func(L):
    """
    Calculate the interquartile range of all elements in a nested list 'L'.
    """
    # Flatten the list
    flat_list = np.array(L).flatten()
    
    # Calculate the interquartile range
    iqr_value = iqr(flat_list)
    
    return iqr_value