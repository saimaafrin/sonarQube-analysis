
import numpy as np
import itertools

def task_func(matrix):
    # Flatten the 2D numpy array to 1D
    flattened = matrix.flatten()
    
    # Sort the flattened array in ascending order
    sorted_array = np.sort(flattened)
    
    # Find all unique combinations of two elements from the sorted array
    unique_combinations = list(itertools.combinations(sorted_array, 2))
    
    # Return the sorted array and the list of unique combinations
    return sorted_array, unique_combinations