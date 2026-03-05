from itertools import zip_longest
from scipy.spatial import distance
def task_func(points):
    """
    Calculate the Euclidean distances between consecutive points in a provided list of 2D coordinates.
    
    :param points: List of tuples, where each tuple contains two numbers representing a point in 2D space.
    :return: list of floats: A list containing the Euclidean distances between consecutive points.
    """
    # Convert single numbers to tuples with both coordinates equal to the number
    points = [(x, x) if isinstance(x, (int, float)) else x for x in points]
    
    # Calculate distances between consecutive points
    distances = [distance.euclidean(p1, p2) for p1, p2 in zip_longest(points, points[1:])]
    
    return distances