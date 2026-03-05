import math
import random
import statistics
RADIUS = 5
def task_func(n):
    """
    Generate n random points within a circle of radius RADIUS (default value is 5) and return their average distance from the center.
    """
    # Generate n random points within a circle of radius RADIUS
    points = [random.uniform(-RADIUS, RADIUS) for _ in range(n)]

    # Calculate the average distance from the center of the circle
    average_distance = statistics.mean(map(lambda x: math.sqrt(x**2 + RADIUS**2), points))

    return average_distance