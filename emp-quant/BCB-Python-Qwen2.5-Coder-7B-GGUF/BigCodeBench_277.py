
import random
from itertools import combinations
import math

def task_func(n):
    if n < 2:
        return None
    
    # Generate n random dots within a unit square
    dots = [(random.random(), random.random()) for _ in range(n)]
    
    # Initialize the minimum distance to a large number
    min_distance = float('inf')
    closest_pair = None
    
    # Check all pairs of dots
    for (x1, y1), (x2, y2) in combinations(dots, 2):
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_pair = ((x1, y1), (x2, y2))
    
    return closest_pair