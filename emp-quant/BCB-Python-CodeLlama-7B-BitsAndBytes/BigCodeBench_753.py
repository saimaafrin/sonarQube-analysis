
import math
import random
import statistics

# Constants
RADIUS = 5

def task_func(n):
    # Generate n random points within a circle of radius RADIUS
    points = []
    for i in range(n):
        theta = random.uniform(0, 2 * math.pi)
        r = random.uniform(0, RADIUS)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        points.append((x, y))

    # Calculate the average distance from the center of the circle
    center = (0, 0)
    distances = [math.sqrt((x - center[0])**2 + (y - center[1])**2) for x, y in points]
    average_distance = statistics.mean(distances)

    return average_distance