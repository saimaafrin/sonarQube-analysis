
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

def task_func(points, seed=0):
    """
    Calculate the Voronoi diagram for a number of points in 2D and plot it.

    Parameters:
    points (np.ndarray): An array of points where each point is represented as [x, y].
    seed (int): Seed for random number generator for reproducibility.

    Returns:
    tuple (vor, ax): A tuple containing:
        vor (Voronoi): A Voronoi object representing the Voronoi diagram of the points.
        ax (Axes): The axes of the plotted Voronoi diagram.
    """
    # Check if the input is valid
    if not isinstance(points, np.ndarray) or points.ndim != 2 or points.shape[1] != 2:
        raise ValueError("Input points must be a 2D numpy array with shape (n_points, 2).")

    # Apply jittering to avoid overlapping points
    np.random.seed(seed)
    jitter = 0.1 * np.random.rand(points.shape[0], 2)
    points_jittered = points + jitter

    # Calculate Voronoi diagram
    vor = Voronoi(points_jittered)

    # Plot the Voronoi diagram
    fig, ax = plt.subplots()
    voronoi_plot_2d(vor, ax=ax)

    return vor, ax