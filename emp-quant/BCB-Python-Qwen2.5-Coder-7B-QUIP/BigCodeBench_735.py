
import numpy as np
from itertools import chain

def task_func(L):
    # Flatten the nested list to a single list
    flattened_list = list(chain.from_iterable(L))
    
    # Calculate the mean and variance
    mean_value = np.mean(flattened_list)
    variance_value = np.var(flattened_list)
    
    # Return the results in a dictionary
    return {'mean': mean_value, 'variance': variance_value}