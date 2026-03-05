
import random
import math
import matplotlib.pyplot as plt

def task_func(points_count=1000, radius=1):
    # Generate random points within a circle
    points = []
    for _ in range(points_count):
        angle = random.uniform(0, 2 * math.pi)
        r = radius * math.sqrt(random.uniform(0, 1))
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        points.append((x, y))
    
    # Convert list of tuples to numpy arrays for plotting
    points = np.array(points)
    
    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(points[:, 0], points[:, 1])
    
    # Set aspect ratio to 'equal' to maintain proportions
    ax.set_aspect('equal')
    
    # Return the Axes object
    return ax