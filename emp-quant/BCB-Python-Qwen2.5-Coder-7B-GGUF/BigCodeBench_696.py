
import numpy as np
import math
import random
from random import uniform

def task_func(radius, num_points):
    points = []
    for _ in range(num_points):
        while True:
            x = uniform(-radius, radius)
            y = uniform(-radius, radius)
            if x**2 + y**2 <= radius**2:
                points.append((x, y))
                break
    return points