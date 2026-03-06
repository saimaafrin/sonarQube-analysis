
import numpy as np
from itertools import chain

def task_func(L):
    # Calculate the mean and variance of all elements in the nested list
    flattened_list = list(chain.from_iterable(L))
    mean = np.mean(flattened_list)
    variance = np.var(flattened_list)

    # Create a dictionary with the mean and variance
    result = {'mean': mean, 'variance': variance}

    return result