
import numpy as np
from itertools import combinations

def task_func(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have the same length.")
    
    # Generate all possible pairs of points
    points = np.array([(x, y) for x, y in combinations(array1, array2)])
    
    # Calculate Euclidean distances between all pairs
    distances = np.sqrt(np.sum((points[:, np.newaxis, :] - points[np.newaxis, :, :]) ** 2, axis=2))
    
    # Return the maximum distance
    return np.max(distances, axis=None)