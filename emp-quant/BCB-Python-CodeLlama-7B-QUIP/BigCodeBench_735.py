
import numpy as np
from itertools import chain

def task_func(L):
    # Calculate the mean and variance of all elements in the list
    mean = np.mean(L)
    variance = np.var(L)
    # Create a dictionary to store the results
    results = {'mean': mean, 'variance': variance}
    return results