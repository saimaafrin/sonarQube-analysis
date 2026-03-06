
import random
import math
import matplotlib.pyplot as plt

def task_func(points_count=1000, radius=1):
    # Generate random points within a circle
    points = []
    for _ in range(points_count):
        angle = 2 * math.pi * random.random()
        r = radius * math.sqrt(random.random())
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        points.append((x, y))
    
    # Convert list of tuples to numpy array for plotting
    points_array = np.array(points)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(points_array[:, 0], points_array[:, 1])
    
    # Set aspect ratio to 'equal'
    ax.set_aspect('equal')
    
    return ax