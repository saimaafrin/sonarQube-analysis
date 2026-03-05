import numpy as np
from scipy.stats import iqr
def task_func(L):
    """
    Calculate the interquartile range of all elements in a nested list 'L'.
    
    Parameters:
    L (list of list of numbers): The nested list of numbers.
    
    Returns:
    iqr_value (float): The interquartile range.
    """
    # Flatten the nested list into a 1D list
    flat_list = [item for sublist in L for item in sublist]
    
    # Calculate the interquartile range using scipy's iqr function
    iqr_value = iqr(flat_list)
    
    return iqr_value