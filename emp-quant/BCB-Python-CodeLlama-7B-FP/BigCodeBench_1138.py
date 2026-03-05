import numpy as np
import itertools
def task_func(matrix):
    """
    Sorts a numeric 2D numpy array in ascending order and finds all unique combinations of two elements from the sorted array.
    The function should output with:
        1. numpy.array: A 1D array with all elements of the input array sorted in ascending order.
        2. list: A list of tuples, each containing a pair of elements from the sorted array, representing all unique combinations taken two at a time.
    """
    # Sort the input array in ascending order
    sorted_array = np.sort(matrix, axis=None)

    # Find all unique combinations of two elements from the sorted array
    unique_combinations = []
    for i in range(len(sorted_array)):
        for j in range(i + 1, len(sorted_array)):
            if sorted_array[i] != sorted_array[j]:
                unique_combinations.append((sorted_array[i], sorted_array[j]))

    return (sorted_array, unique_combinations)
matrix = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])