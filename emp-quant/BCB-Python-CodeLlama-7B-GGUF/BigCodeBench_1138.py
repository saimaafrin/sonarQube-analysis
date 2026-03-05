
import numpy as np
import itertools

def task_func(matrix):
    # Sort the 2D array in ascending order
    sorted_array = np.sort(matrix, axis=None)

    # Find all unique combinations of two elements from the sorted array
    unique_combinations = list(itertools.combinations(sorted_array.flatten(), 2))

    # Return a tuple containing the sorted array and the list of unique combinations
    return (sorted_array, unique_combinations)