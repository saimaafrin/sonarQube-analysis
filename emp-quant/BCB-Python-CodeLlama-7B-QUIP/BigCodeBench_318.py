
import random
import math
import matplotlib.pyplot as plt

def task_func(points_count=1000, radius=1):
    # Generate points within the circle
    points = []
    for i in range(points_count):
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)
        points.append((x, y))

    # Plot the points
    fig, ax = plt.subplots()
    ax.scatter(points)
    ax.set_aspect('equal')
    ax.set_xlim(-radius, radius)
    ax.set_ylim(-radius, radius)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Random points within a circle')
    return ax