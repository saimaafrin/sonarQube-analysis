from itertools import zip_longest
from scipy.spatial import distance
def task_func(points):
    """
    Calculate the Euclidean distances between consecutive points in a provided list of 2D coordinates.
    This function takes a list of tuples, where each tuple contains two numbers representing a point in 2D space.
    It computes the Euclidean distance between each consecutive pair of points.
    If an empty list or a single point is passed, the function returns an empty list.
    If a tuple contains just one number it is assumed that both coordinates are equal to this number.
    """
    # Check if the input is valid
    if not points or len(points) == 1:
        return []

    # Compute the Euclidean distances between consecutive points
    distances = []
    for i in range(len(points) - 1):
        point1 = points[i]
        point2 = points[i + 1]
        distances.append(distance.euclidean(point1, point2))

    return distances
points = [(1, 2), (4), (-1.2, 4)]