import math
import random
import statistics
RADIUS = 5
def task_func(n):
    """
    Generate n random points within a circle of radius RADIUS and return their average distance from the center.
    """
    # Generate n random points within a circle of radius RADIUS
    points = []
    for _ in range(n):
        x = random.uniform(-RADIUS, RADIUS)
        y = random.uniform(-RADIUS, RADIUS)
        points.append((x, y))

    # Calculate the average distance from the center of the circle
    distances = []
    for point in points:
        distances.append(math.sqrt(point[0]**2 + point[1]**2))
    average_distance = statistics.mean(distances)

    return average_distance