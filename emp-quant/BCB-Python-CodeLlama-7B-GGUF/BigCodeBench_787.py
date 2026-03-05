
import numpy as np
from itertools import combinations

def task_func(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have the same length")

    points = [(x, y) for x, y in combinations(zip(array1, array2), 2)]
    distances = [np.linalg.norm(p1 - p2) for p1, p2 in points]
    return max(distances)