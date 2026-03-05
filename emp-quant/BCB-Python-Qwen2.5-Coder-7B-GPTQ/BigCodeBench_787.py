import numpy as np
from itertools import combinations
def task_func(array1, array2):
    """
    Calculate the maximum Euclidean distance between all possible pairs of points formed by combining elements from two input arrays.
    
    Parameters:
    array1 (list): The first input array.
    array2 (list): The second input array.
    
    Returns:
    max_distance (float): The maximum Euclidean distance between any two points formed by combining elements from array1 and array2.
    """
    # Check if the input arrays have different lengths
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have the same length.")
    
    # If the arrays are empty, return 0
    if not array1 or not array2:
        return 0
    
    # Generate all possible pairs of points
    points = [(x, y) for x in array1 for y in array2]
    
    # Calculate the Euclidean distance for each pair and find the maximum
    max_distance = max(np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) for (x1, y1), (x2, y2) in combinations(points, 2))
    
    return max_distance