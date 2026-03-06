
import numpy as np
import math
import random
from random import uniform

def task_func(radius, num_points):
    # Generate a list of random points within a circle
    points = []
    for i in range(num_points):
        theta = uniform(0, 2 * math.pi)
        r = uniform(0, radius)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        points.append((x, y))
    return points