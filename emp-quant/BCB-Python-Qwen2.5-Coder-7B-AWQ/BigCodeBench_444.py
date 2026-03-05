import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def task_func(n_points=100, random_seed=None):
    """
    Generate an array of random 3D dots and draw them in a 3D scatter plot.

    Parameters:
    n_points (int): The number of points to generate.
    random_seed (int, optional): Seed for the random number generator for reproducibility.

    Returns:
    tuple: A tuple containing:
        points (ndarray): A numpy ndarray of shape (n_points, 3) with the coordinates of the points.
        plot (Axes3D): A 3D scatter plot of the generated points.
    """
    # Set the random seed if provided
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate random points in the range [0, 1) for each dimension
    points = np.random.rand(n_points, 3)
    
    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2])
    
    # Return the points and the plot
    return points, ax