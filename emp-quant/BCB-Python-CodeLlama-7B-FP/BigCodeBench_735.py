import numpy as np
from itertools import chain
def task_func(L):
    """
    Calculate the mean and variance of all elements in a nested list 'L'.
    """
    # Flatten the list
    flat_list = list(chain.from_iterable(L))

    # Calculate the mean
    mean = np.mean(flat_list)

    # Calculate the variance
    variance = np.var(flat_list)

    # Return a dictionary containing the mean and variance
    return {'mean': mean, 'variance': variance}
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]