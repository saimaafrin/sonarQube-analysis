
import numpy as np
from itertools import chain

def task_func(L):
    # Flatten the nested list
    flat_list = list(chain.from_iterable(L))
    
    # Calculate the mean and variance
    mean = np.mean(flat_list)
    variance = np.var(flat_list)
    
    # Return a dictionary containing the mean and variance
    return {'mean': mean, 'variance': variance}