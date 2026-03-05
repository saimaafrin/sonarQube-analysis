
import numpy as np
import matplotlib.pyplot as plt

def task_func(n_points=100, random_seed=None):
    # Set the random seed if provided
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random points in the range [0, 1) for each dimension
    points = np.random.rand(n_points, 3)
    
    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='b', marker='o')
    
    # Return the points and the plot
    return points, ax