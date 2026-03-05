
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

def task_func(points, seed=0):
    """
    Calculate the Voronoi diagram for a number of points in 2D and plot it.
    
    Parameters:
    points (np.ndarray): A 2D array of points with shape (n, 2).
    seed (int): Seed for random number generator to ensure reproducibility.
    
    Returns:
    tuple: A tuple containing the Voronoi object and the axes of the plotted Voronoi diagram.
    """
    # Check if the input is a numpy array
    if not isinstance(points, np.ndarray):
        raise TypeError("Input points must be a numpy array.")
    
    # Check if the shape of the input array is correct
    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError("Input points must have shape (n, 2).")
    
    # Apply jittering to the points
    np.random.seed(seed)
    jitter = 0.1 * np.random.rand(points.shape[0], 2)
    points_jittered = points + jitter
    
    # Calculate the Voronoi diagram
    vor = Voronoi(points_jittered)
    
    # Plot the Voronoi diagram
    fig, ax = plt.subplots()
    voronoi_plot_2d(vor, ax=ax)
    
    return vor, ax