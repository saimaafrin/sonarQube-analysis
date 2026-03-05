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
    smallest_distance = float('inf')
    
    # Iterate over all pairs of points to find the closest pair
    for (x1, y1), (x2, y2) in combinations(points, 2):
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if distance < smallest_distance:
            smallest_distance = distance
            closest_pair = ((x1, y1), (x2, y2))
    
    return closest_pair