import random
from itertools import combinations
import math
def task_func(n):
    if n < 2:
        return None
    points = [(random.random(), random.random()) for _ in range(n)]
    closest_pair = None
    closest_distance = math.inf
    for i, j in combinations(points, 2):
        distance = math.sqrt((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2)
        if distance < closest_distance:
            closest_distance = distance
            closest_pair = (i, j)
    return closest_pair