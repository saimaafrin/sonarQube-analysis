
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def task_func(n_points=100, random_seed=None):
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random 3D points
    points = np.random.rand(n_points, 3)
    
    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='b', marker='o')
    
    # Set labels for the axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # Return the points and the plot
    return points, ax