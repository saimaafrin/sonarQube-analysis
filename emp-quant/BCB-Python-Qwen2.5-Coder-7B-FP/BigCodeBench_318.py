import random
import math
import matplotlib.pyplot as plt
def task_func(points_count=1000, radius=1):
    """
    Generate a specified number of random points within a circle of a given radius and plot them using a scatter plot.
    
    Parameters:
    - points_count: int, the number of points to generate.
    - radius: float, the radius of the circle.
    
    Returns:
    - Axes: The matplotlib Axes object representing the scatter plot.
    """
    # Generate random points within the circle
    points = []
    for _ in range(points_count):
        while True:
            x = random.uniform(-radius, radius)
            y = random.uniform(-radius, radius)
            if x**2 + y**2 <= radius**2:
                points.append((x, y))
                break
    
    # Extract x and y coordinates
    x_coords, y_coords = zip(*points)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x_coords, y_coords)
    ax.set_aspect('equal')
    
    return ax