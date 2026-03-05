import numpy as np
from itertools import combinations
def task_func(array1, array2):
    """
    Calculate the maximum Euclidean distance between all possible pairs of points formed by combining elements from two input arrays. Each point is formed by combining one element from the first array and one element from the second array. The function then calculates the Euclidean distance between each pair of points and returns the maximum distance found.
    The function should raise the exception for: ValueError: If the input arrays have different lengths.
    The function should output with:
        max_distance (float): The maximum Euclidean distance between any two points formed by combining
        elements from array1 and array2. If the arrays are empty, the function
        returns 0.
    """
    if len(array1) != len(array2):
        raise ValueError("Input arrays have different lengths.")

    # Calculate the maximum Euclidean distance between all possible pairs of points
    max_distance = 0
    for point1, point2 in combinations(array1, array2):
        distance = np.linalg.norm(point1 - point2)
        if distance > max_distance:
            max_distance = distance

    return max_distance
array1 = [1, 2, 3]
array2 = [4, 5, 6]