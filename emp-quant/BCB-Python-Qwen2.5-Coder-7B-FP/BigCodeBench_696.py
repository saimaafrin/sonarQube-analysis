import numpy as np
import math
import random
from random import uniform
def task_func(radius, num_points):
    """
    Generate a list of random points within a circle of a given radius.

    Parameters:
    radius (float): The radius of the circle.
    num_points (int): The number of points to generate.

    Returns:
    out (list): A list of points within the circle.
    """
    points = []
    for _ in range(num_points):
        while True:
            x = uniform(-radius, radius)
            y = uniform(-radius, radius)
            if x**2 + y**2 <= radius**2:
                points.append((x, y))
                break
    return points
radius = 5
num_points = 10