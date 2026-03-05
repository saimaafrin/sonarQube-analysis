import numpy as np
from itertools import product
def task_func(array1, array2):
    """
    Calculate the maximum Euclidean distance between all possible pairs of points formed by combining
    elements from two input arrays. Each point is formed by combining one element from the first array
    and one element from the second array. The function then calculates the Euclidean distance between
    each pair of points and returns the maximum distance found.
    
    Parameters:
    array1 (np.array): The first input array.
    array2 (np.array): The second input array.
    
    Returns:
    max_distance (float): The maximum Euclidean distance between any two points formed by combining
    elements from array1 and array2. If the arrays are empty, the function returns 0.
    
    Raises:
    ValueError: If the input arrays have different lengths.
    """
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have the same length.")
    
    if len(array1) == 0:
        return 0
    
    # Generate all possible pairs of points
    points = list(product(array1, array2))
    
    # Calculate the Euclidean distance for each pair
    distances = [np.linalg.norm(np.array(point1) - np.array(point2)) for point1, point2 in combinations(points, 2)]
    
    # Return the maximum distance
    return max(distances)