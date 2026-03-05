import numpy as np
import matplotlib.pyplot as plt
def task_func(n_points=100, random_seed=None):
    """
    Generate an array of random 3D dots in the range [0, 1) for each dimension and draw them in a 3D scatter plot.

    Args:
        n_points (int, optional): Number of points to generate. Defaults to 100.
        random_seed (int, optional): Random seed to use for reproducibility. Defaults to None.

    Returns:
        tuple: A tuple containing:
            points (ndarray): A numpy ndarray of shape (n_points, 3) with the coordinates of the points.
            plot (Axes3D): A 3D scatter plot of the generated points.
    """
    # Set random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)

    # Generate random points in the range [0, 1) for each dimension
    points = np.random.rand(n_points, 3)

    # Create a 3D scatter plot of the points
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='r')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Scatter Plot of Random Points')

    return points, ax
n_points = 100
random_seed = 42