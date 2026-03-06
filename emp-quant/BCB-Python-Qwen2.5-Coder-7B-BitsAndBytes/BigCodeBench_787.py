
import numpy as np
from itertools import product

def task_func(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have the same length.")
    
    # Generate all possible pairs of points
    points = list(product(array1, array2))
    
    # Calculate the Euclidean distance for each pair
    distances = [np.linalg.norm(np.array(point1) - np.array(point2)) for point1, point2 in combinations(points, 2)]
    
    # Return the maximum distance
    return max(distances) if distances else 0