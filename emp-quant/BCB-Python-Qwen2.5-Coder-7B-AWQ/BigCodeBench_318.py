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
        angle = 2 * math.pi * random.random()
        r = radius * math.sqrt(random.random())
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        points.append((x, y))
    
    # Convert list of points to numpy arrays for plotting
    x, y = zip(*points)
    
    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_aspect('equal')  # Set aspect ratio to 'equal' to maintain proportions
    
    return ax