import math
import random
import statistics
RADIUS = 5
def task_func(n):
    """
    Generate n random points within a circle of radius RADIUS and return their average distance from the center.
    
    Parameters:
    n (int): The number of random points to generate.
    
    Returns:
    float: The average distance from the center of the circle.
    """
    total_distance = 0
    
    for _ in range(n):
        # Generate random angle and radius
        angle = 2 * math.pi * random.random()
        radius = RADIUS * math.sqrt(random.random())
        
        # Convert polar coordinates to Cartesian coordinates
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        
        # Calculate distance from the center
        distance = math.sqrt(x**2 + y**2)
        total_distance += distance
    
    # Calculate average distance
    average_distance = total_distance / n
    return average_distance
n = 1000