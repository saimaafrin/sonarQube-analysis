import numpy as np
from functools import reduce
def task_func(list_of_pairs):
    """
    Calculate the product of the second values in each tuple in a list of tuples and return the product as a single-element numeric array.
    """
    # Calculate the product of the second values in each tuple
    product = reduce(lambda x, y: x * y[1], list_of_pairs, 1)

    # Return the product as a single-element numeric array
    return np.array([product])
list_of_pairs = [(1, 2), (3, 4), (5, 6)]