import math
import random
import statistics
RADIUS = 5
def task_func(n):
    """
    Generate n random points within a circle of radius RADIUS and return their average distance from the center.
    """
    # Generate n random points within a circle of radius RADIUS
    points = [
        (random.uniform(-RADIUS, RADIUS), random.uniform(-RADIUS, RADIUS))
        for _ in range(n)
    ]

    # Calculate the average distance from the center of the circle
    distances = [math.sqrt(x**2 + y**2) for x, y in points]
    average_distance = statistics.mean(distances)

    return average_distance