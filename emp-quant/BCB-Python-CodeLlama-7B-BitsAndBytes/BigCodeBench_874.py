
from itertools import zip_longest
from scipy.spatial import distance

def task_func(points):
    # Check if the input is a list of tuples
    if not isinstance(points, list) or not all(isinstance(point, tuple) for point in points):
        raise ValueError("Input must be a list of tuples")

    # Check if the list is empty or has only one element
    if len(points) < 2:
        return []

    # Compute the Euclidean distances between consecutive points
    distances = []
    for i in range(len(points) - 1):
        point1, point2 = points[i], points[i + 1]
        if len(point1) == 1:
            point1 = (point1[0], point1[0])
        if len(point2) == 1:
            point2 = (point2[0], point2[0])
        distances.append(distance.euclidean(point1, point2))

    return distances