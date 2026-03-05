
import random
import math
import matplotlib.pyplot as plt

def task_func(points_count=1000, radius=1):
    # Generate random points within a circle
    points = []
    while len(points) < points_count:
        x, y = random.random() * 2 - 1, random.random() * 2 - 1
        if math.sqrt(x**2 + y**2) <= radius:
            points.append((x, y))

    # Plot the points
    fig, ax = plt.subplots()
    ax.scatter([x for x, y in points], [y for x, y in points], s=1)
    ax.set_aspect('equal')
    plt.show()

    return ax