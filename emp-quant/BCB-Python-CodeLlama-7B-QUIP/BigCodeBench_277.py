
import random
from itertools import combinations
import math

def task_func(n):
    if n < 2:
        return None
    points = [(random.random(), random.random()) for _ in range(n)]
    closest_pair = min(combinations(points, 2), key=lambda x: math.dist(x[0][0], x[1][0]) + math.dist(x[0][1], x[1][1])
    return (closest_pair[0][0], closest_pair[1][0]), (closest_pair[0][1], closest_pair[1][1]))