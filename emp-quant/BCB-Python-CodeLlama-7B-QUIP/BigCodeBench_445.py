
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

def task_func(points, seed=0):
    # Check if input is valid
    if not isinstance(points, np.ndarray):
        raise ValueError("Input must be a numpy array")
    if len(points.shape) != 2:
        raise ValueError("Input must be a 2D array")

    # Jitter the points
    points += np.random.RandomState(seed).rand(2, points.shape[1])

    # Create the Voronoi object
    vor = Voronoi(points)

    # Plot the Voronoi diagram
    ax = voronoi_plot_2d(vor, points)

    return vor, ax