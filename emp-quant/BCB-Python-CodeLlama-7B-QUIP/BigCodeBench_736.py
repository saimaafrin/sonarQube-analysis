
import numpy as np
from scipy import stats

def task_func(L):
    # Calculate the mode of the list
    mode = stats.mode(L)
    return mode