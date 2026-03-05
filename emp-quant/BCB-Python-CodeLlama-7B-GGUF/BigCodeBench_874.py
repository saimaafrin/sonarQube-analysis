
from itertools import zip_longest
from scipy.spatial import distance

def task_func(points):
    if not points or len(points) == 1:
        return []

    distances = []
    for i in range(len(points) - 1):
        p1, p2 = points[i], points[i + 1]
        if len(p1) == 1:
            p1 = (p1[0], p1[0])
        if len(p2) == 1:
            p2 = (p2[0], p2[0])
        distances.append(distance.euclidean(p1, p2))

    return distances