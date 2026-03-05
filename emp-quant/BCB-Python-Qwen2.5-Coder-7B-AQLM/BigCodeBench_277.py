
import random
from itertools import combinations
import math

def task_func(n):
    if n < 2:
        return None
    
    # Generate n random dots within a unit square
    dots = [(random.random(), random.random()) for _ in range(n)]
    
    # Initialize variables to store the closest pair and the smallest distance
    closest_pair = None
    smallest_distance = float('inf')
    
    # Iterate over all pairs of dots to find the closest pair
    for dot1, dot2 in combinations(dots, 2):
        distance = math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)
        if distance < smallest_distance:
            smallest_distance = distance
            closest_pair = (dot1, dot2)
    
    return closest_pair