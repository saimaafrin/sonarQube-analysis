
from itertools import zip_longest
from scipy.spatial import distance

def task_func(points):
    if len(points) < 2:
        return []
    distances = []
    for i in range(len(points) - 1):
        distances.append(distance.euclidean(points[i], points[i + 1]))
    return distances