import random
import math
import matplotlib.pyplot as plt
def task_func(points_count=1000, radius=1):
    """
    Generate a specified (i.e., points_counts) number of random points within a circle of a given radius and plot them using a scatter plot.
    Note that: All settings of the scatter plot are the default version. The aspect ratio of the plot is set to 'equal' to maintain proportions.
    The function should output with:
        Axes: The matplotlib Axes object representing the scatter plot.
    """
    # Generate random points within the circle
    points = []
    for _ in range(points_count):
        theta = random.uniform(0, 2 * math.pi)
        r = random.uniform(0, radius)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        points.append((x, y))

    # Create the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(points)
    ax.set_aspect('equal')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Random Points within a Circle')

    return ax
points_count = 1000
radius = 1