
import numpy as np
from functools import reduce

def task_func(list_of_pairs):
    # Extract the second elements from each tuple
    second_values = [pair[1] for pair in list_of_pairs]
    # Calculate the product of the second values
    product = reduce(lambda x, y: x * y, second_values)
    # Return the product as a 1D numpy array
    return np.array([product])