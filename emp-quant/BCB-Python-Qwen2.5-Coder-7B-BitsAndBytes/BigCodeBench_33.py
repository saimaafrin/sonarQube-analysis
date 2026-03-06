
import numpy as np
from functools import reduce

def task_func(list_of_pairs):
    """
    Calculate the product of the second values in each tuple in a list of tuples.

    Parameters:
    list_of_pairs (list of tuples): A list where each element is a tuple of two elements.

    Returns:
    numpy.ndarray: A 1D numpy array containing a single element that is the product of the second values in the list of tuples.
    """
    # Extract the second value from each tuple using a lambda function
    second_values = [pair[1] for pair in list_of_pairs]
    
    # Use reduce to multiply all the second values together
    product = reduce(lambda x, y: x * y, second_values)
    
    # Return the product as a 1D numpy array
    return np.array([product])