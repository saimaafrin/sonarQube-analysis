
import numpy as np
from itertools import combinations

def task_func(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have the same length")

    max_distance = 0
    for point1, point2 in combinations(array1, 2):
        distance = np.linalg.norm(point1 - point2)
        if distance > max_distance:
            max_distance = distance

    return max_distance