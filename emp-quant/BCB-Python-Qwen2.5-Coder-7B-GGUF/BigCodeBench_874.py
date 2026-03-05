
from itertools import zip_longest
from scipy.spatial import distance

def task_func(points):
    if len(points) < 2:
        return []
    
    distances = []
    for point1, point2 in zip_longest(points, points[1:], fillvalue=(0, 0)):
        if len(point1) == 1:
            point1 = (point1[0], point1[0])
        if len(point2) == 1:
            point2 = (point2[0], point2[0])
        dist = distance.euclidean(point1, point2)
        distances.append(dist)
    
    return distances