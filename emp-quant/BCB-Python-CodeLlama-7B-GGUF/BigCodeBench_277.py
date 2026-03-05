
import random
from itertools import combinations
import math

def task_func(n):
    if n < 2:
        return None

    # Generate n random dots within a unit square
    dots = [(random.random(), random.random()) for _ in range(n)]

    # Find the pair that comes closest to each other
    closest_pair = None
    closest_distance = math.inf
    for i, j in combinations(range(n), 2):
        distance = math.sqrt((dots[i][0] - dots[j][0]) ** 2 + (dots[i][1] - dots[j][1]) ** 2)
        if distance < closest_distance:
            closest_distance = distance
            closest_pair = (dots[i], dots[j])

    return closest_pair