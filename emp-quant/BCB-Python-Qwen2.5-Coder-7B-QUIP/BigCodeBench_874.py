
from itertools import zip_longest
from scipy.spatial import distance

def task_func(points):
    # Filter out points that do not have two coordinates
    valid_points = [(x, y) for x, y in points if isinstance(x, (int, float)) and isinstance(y, (int, float))]
    
    # If there are less than 2 valid points, return an empty list
    if len(valid_points) < 2:
        return []
    
    # Calculate the Euclidean distance between consecutive points
    distances = [distance.euclidean(point1, point2) for point1, point2 in zip_longest(valid_points, valid_points[1:], fillvalue=valid_points[0])]
    
    return distances