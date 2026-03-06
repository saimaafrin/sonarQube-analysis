
import numpy as np
from functools import reduce

def task_func(list_of_pairs):
    # Calculate the product of the second values in each tuple
    product = reduce(lambda x, y: x * y, [pair[1] for pair in list_of_pairs])

    # Return the product as a single-element numpy array
    return np.array([product])