
import math
import random
import statistics

# Constants
RADIUS = 5

def task_func(n):
    # Generate n random points within a circle of radius RADIUS
    points = [random.uniform(-RADIUS, RADIUS) for _ in range(n)]

    # Calculate the average distance from the center of the circle
    center = (0, 0)
    distances = [math.hypot(p[0] - center[0], p[1] - center[1]) for p in points]
    average_distance = statistics.mean(distances)

    return average_distance