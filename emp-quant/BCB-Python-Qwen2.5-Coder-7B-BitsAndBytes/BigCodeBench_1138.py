
import numpy as np
import itertools

def task_func(matrix):
    # Flatten the matrix to a 1D array
    flat_array = matrix.flatten()
    
    # Sort the flattened array in ascending order
    sorted_array = np.sort(flat_array)
    
    # Find all unique combinations of two elements from the sorted array
    combinations = list(itertools.combinations(sorted_array, 2))
    
    return (sorted_array, combinations)