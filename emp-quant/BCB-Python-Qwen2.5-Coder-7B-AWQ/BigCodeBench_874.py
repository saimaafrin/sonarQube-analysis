from itertools import zip_longest
from scipy.spatial import distance
def task_func(points):
    """
    Calculate the Euclidean distances between consecutive points in a provided list of 2D coordinates.
    
    :param points: List of tuples, where each tuple contains two numbers representing a point in 2D space.
    :return: list of floats: A list containing the Euclidean distances between consecutive points.
    """
    # Convert single number tuples to tuples with equal coordinates
    points = [(x, x) if len(p) == 1 else p for p in points]
    
    # Calculate distances between consecutive points
    distances = [distance.euclidean(p1, p2) for p1, p2 in zip(points, points[1:])]
    
    return distances