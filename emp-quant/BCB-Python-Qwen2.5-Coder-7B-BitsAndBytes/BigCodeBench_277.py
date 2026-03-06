
import random
from itertools import combinations
import math

def task_func(n):
    if n < 2:
        return None
    
    # Generate n random points in the unit square
    points = [(random.random(), random.random()) for _ in range(n)]
    
    # Initialize variables to store the closest pair and the smallest distance
    closest_pair = None
    min_distance = float('inf')
    
    # Iterate over all pairs of points to find the closest pair
    for point1, point2 in combinations(points, 2):
        distance = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_pair = (point1, point2)
    
    return closest_pair