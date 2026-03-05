
import numpy as np
from itertools import combinations

def task_func(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have the same length")
    
    if not array1 and not array2:
        return 0
    
    max_distance = 0
    for point1, point2 in combinations([(x, y) for x in array1 for y in array2], 2):
        distance = np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
        if distance > max_distance:
            max_distance = distance
    
    return max_distance