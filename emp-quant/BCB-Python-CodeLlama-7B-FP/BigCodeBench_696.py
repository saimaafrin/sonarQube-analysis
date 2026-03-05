import numpy as np
import math
import random
from random import uniform
def task_func(radius, num_points):
    """
    Create a tuple with a list of random points within a circle of a given radius.
    """
    # Generate random points within a circle
    points = []
    for _ in range(num_points):
        x = uniform(0, radius)
        y = uniform(0, radius)
        points.append((x, y))

    # Check if points are within the circle
    for point in points:
        if math.sqrt(point[0]**2 + point[1]**2) > radius:
            raise ValueError("Point is outside of the circle")

    return points
radius = 10
num_points = 100