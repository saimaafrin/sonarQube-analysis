import math
import random
import statistics
RADIUS = 5
def task_func(n):
    # Generate n random points within a circle of radius RADIUS
    points = []
    for _ in range(n):
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(0, RADIUS)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        points.append((x, y))
    
    # Calculate the average distance from the center of the circle
    distances = [math.sqrt(x**2 + y**2) for x, y in points]
    average_distance = statistics.mean(distances)
    
    return average_distance