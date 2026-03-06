
from itertools import zip_longest
from scipy.spatial import distance

def task_func(points):
    if len(points) < 2:
        return []
    
    # Ensure all points have exactly two coordinates
    points = [(x[0], x[1] if len(x) > 1 else x[0]) for x in points]
    
    # Calculate Euclidean distances between consecutive points
    distances = [distance.euclidean(p1, p2) for p1, p2 in zip(points[:-1], points[1:])]
    
    return distances