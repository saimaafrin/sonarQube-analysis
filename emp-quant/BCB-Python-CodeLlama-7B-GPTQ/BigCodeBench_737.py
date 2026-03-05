import numpy as np
import math
def task_func(L):
    """
    Calculate the median of all elements in a nested list 'L'.
    """
    # Check if the input is a list
    if not isinstance(L, list):
        raise ValueError("Input must be a list")

    # Check if the list is empty
    if len(L) == 0:
        raise ValueError("Input list is empty")

    # Flatten the list
    flattened_list = [item for sublist in L for item in sublist]

    # Sort the flattened list
    sorted_list = sorted(flattened_list)

    # Calculate the median
    median = sorted_list[len(sorted_list) // 2]

    # Check if the list has an even number of elements
    if len(sorted_list) % 2 == 0:
        median = (median + sorted_list[len(sorted_list) // 2 - 1]) / 2

    return median
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]