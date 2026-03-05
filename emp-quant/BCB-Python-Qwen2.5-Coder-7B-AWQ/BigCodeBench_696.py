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
        angle = uniform(0, 2 * math.pi)
        distance = uniform(0, radius)
        x = distance * math.cos(angle)
        y = distance * math.sin(angle)
        points.append((x, y))
    return points
radius = 5
num_points = 10