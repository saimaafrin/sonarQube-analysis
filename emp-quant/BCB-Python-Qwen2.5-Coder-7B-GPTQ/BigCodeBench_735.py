import numpy as np
from itertools import chain
def task_func(L):
    # Flatten the nested list using chain from itertools
    flattened_list = list(chain.from_iterable(L))
    
    # Calculate the mean of the flattened list
    mean_value = np.mean(flattened_list)
    
    # Calculate the variance of the flattened list
    variance_value = np.var(flattened_list)
    
    # Return the results in a dictionary
    return {'mean': mean_value, 'variance': variance_value}