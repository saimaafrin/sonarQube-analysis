
import math
import random
import statistics
# Constants
RADIUS = 5

def task_func(n):
    total_distance = 0
    for _ in range(n):
        # Generate random angle and radius
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(0, RADIUS)
        # Convert polar coordinates to Cartesian coordinates
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        # Calculate distance from the center
        distance = math.sqrt(x**2 + y**2)
        total_distance += distance
    # Calculate average distance
    average_distance = total_distance / n
    return average_distance