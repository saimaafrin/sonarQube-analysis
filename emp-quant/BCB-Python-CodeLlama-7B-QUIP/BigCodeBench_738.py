
import numpy as np
from scipy.stats import iqr

def task_func(L):
    # Calculate the interquartile range of all elements in the list
    iqr_value = iqr(L)
    return iqr_value