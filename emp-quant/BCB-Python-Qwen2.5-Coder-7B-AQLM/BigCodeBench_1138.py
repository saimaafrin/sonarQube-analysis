
import numpy as np
import itertools

def task_func(matrix):
    # Sort the 2D numpy array in ascending order
    sorted_array = np.sort(matrix)
    
    # Flatten the sorted array to a 1D array
    flattened_array = sorted_array.flatten()
    
    # Find all unique combinations of two elements from the sorted array
    unique_combinations = list(itertools.combinations(flattened_array, 2))
    
    # Return the sorted array and the list of unique combinations
    return (flattened_array, unique_combinations)