
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

    # Iterate through all pairs of dots
    for dot1, dot2 in combinations(dots, 2):
        # Calculate the Euclidean distance between the two dots
        distance = math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)
        # Update the minimum distance and closest pair if the current distance is smaller
        if distance < min_distance:
            min_distance = distance
            closest_pair = (dot1, dot2)

    return closest_pair