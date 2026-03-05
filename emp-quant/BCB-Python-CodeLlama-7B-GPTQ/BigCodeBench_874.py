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
    if not points:
        return []
    if len(points) == 1:
        return []
    return [distance.euclidean(p1, p2) for p1, p2 in zip_longest(points, points[1:])]