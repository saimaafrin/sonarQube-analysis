
import numpy as np
from scipy import stats

def task_func(L):
    # Flatten the nested list to a 1D array
    flattened = np.array(L).flatten()
    
    # Calculate the mode
    mode = stats.mode(flattened)[0]
    
    return mode