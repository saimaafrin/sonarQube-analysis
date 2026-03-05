import numpy as np
import itertools
def task_func(matrix):
    """
    Sorts a numeric 2D numpy array in ascending order and finds all unique combinations of two elements from the sorted array.
    
    Parameters:
    matrix (np.array): A 2D numpy array of numeric values.
    
    Returns:
    tuple: A tuple containing two elements:
        1. numpy.array: A 1D array with all elements of the input array sorted in ascending order.
        2. list: A list of tuples, each containing a pair of elements from the sorted array, representing all unique combinations taken two at a time.
    """
    # Flatten the 2D array and sort it
    sorted_array = np.sort(matrix.flatten())
    
    # Generate all unique combinations of two elements from the sorted array
    combinations = list(itertools.combinations(sorted_array, 2))
    
    return sorted_array, combinations
matrix = np.array([[3, 1, 4], [1, 5, 9]])