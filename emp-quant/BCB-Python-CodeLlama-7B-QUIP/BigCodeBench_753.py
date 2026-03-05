
import math
import random
import statistics

# Constants
RADIUS = 5

def task_func(n):
    # Generate n random points within a circle of radius RADIUS
    points = [random.uniform(-RADIUS, RADIUS) for i in range(n)]
    # Calculate the average distance from the center of the circle
    avg_dist = statistics.mean(map(lambda x: math.dist(x, 0), points))
    return avg_dist