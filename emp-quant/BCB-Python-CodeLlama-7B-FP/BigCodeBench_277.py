import random
from itertools import combinations
import math
def task_func(n):
    if n < 2:
        return None
    points = [(random.random(), random.random()) for _ in range(n)]
    closest_pair = None
    closest_distance = math.inf
    for p1, p2 in combinations(points, 2):
        distance = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        if distance < closest_distance:
            closest_pair = (p1, p2)
            closest_distance = distance
    return closest_pair