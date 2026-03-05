
import numpy as np
import math
import random
from random import uniform
def task_func(radius, num_points):
    points = []
    for _ in range(num_points):
        angle = uniform(0, 2 * math.pi)
        distance = uniform(0, radius)
        x = distance * math.cos(angle)
        y = distance * math.sin(angle)
        points.append((x, y))
    return points