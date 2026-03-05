import numpy as np
from functools import reduce
def task_func(list_of_pairs):
    """
    Calculate the product of the second values in each tuple in a list of tuples and return the product as a single-element numeric array.
    
    Parameters:
    list_of_pairs (list of tuples): A list where each element is a tuple of two numeric values.
    
    Returns:
    numpy.ndarray: A 1D numpy array containing a single element that is the product of the second values in the list of tuples.
    """
    # Extract the second elements from each tuple
    second_values = [pair[1] for pair in list_of_pairs]
    
    # Calculate the product of the second values
    product = reduce(lambda x, y: x * y, second_values)
    
    # Return the product as a single-element numpy array
    return np.array([product])
list_of_pairs = [(1, 2), (3, 4), (5, 6)]