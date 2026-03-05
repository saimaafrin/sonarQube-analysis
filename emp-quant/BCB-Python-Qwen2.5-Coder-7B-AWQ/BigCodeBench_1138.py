import numpy as np
import itertools
def task_func(matrix):
    # Flatten the 2D numpy array and sort it
    sorted_array = np.sort(matrix.flatten())
    
    # Find all unique combinations of two elements from the sorted array
    combinations = list(itertools.combinations(sorted_array, 2))
    
    return sorted_array, combinations
matrix = np.array([[3, 1, 4], [1, 5, 9]])