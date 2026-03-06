
import math
import random
import statistics

# Constants
RADIUS = 5

def task_func(n):
    # Generate n random points within the circle
    points = []
    for _ in range(n):
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(0, RADIUS)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        points.append((x, y))
    
    # Calculate distances from the center to each point
    distances = [math.sqrt(x**2 + y**2) for x, y in points]
    
    # Return the average distance
    return statistics.mean(distances)