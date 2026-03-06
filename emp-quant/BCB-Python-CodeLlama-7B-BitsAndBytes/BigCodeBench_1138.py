
import numpy as np
import itertools

def task_func(matrix):
    # Sort the array in ascending order
    sorted_array = np.sort(matrix)

    # Find all unique combinations of two elements from the sorted array
    unique_combinations = []
    for i in range(len(sorted_array)):
        for j in range(i+1, len(sorted_array)):
            if sorted_array[i] != sorted_array[j]:
                unique_combinations.append((sorted_array[i], sorted_array[j]))

    return (sorted_array, unique_combinations)