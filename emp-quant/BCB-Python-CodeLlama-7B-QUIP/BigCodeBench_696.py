
import numpy as np
import math
import random
from random import uniform

def task_func(radius, num_points):
    # Generate a list of random points within the circle
    points = [uniform(-radius, radius) for i in range(num_points)]
    # Sort the points by their distance from the center of the circle
    sorted_points = sorted(points, key=lambda x: math.dist(0, 0, x))
    # Return the list of points
    return sorted_points