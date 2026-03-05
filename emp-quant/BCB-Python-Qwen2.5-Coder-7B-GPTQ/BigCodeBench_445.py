import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
def task_func(points, seed=0):
    """
    Calculate the Voronoi diagram for a number of points in 2D and plot it.
    
    Parameters:
    - points (np.ndarray): A 2D array of points where each row represents a point.
    - seed (int): Seed for the random number generator for jittering.
    
    Returns:
    - tuple: A tuple containing the Voronoi object and the axes of the plotted Voronoi diagram.
    """
    # Check if the input is a numpy array
    if not isinstance(points, np.ndarray):
        raise TypeError("Input points must be a numpy array.")
    
    # Check if the input array has the correct shape
    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError("Input points must be a 2D array with shape (n_points, 2).")
    
    # Apply jittering
    np.random.seed(seed)
    jitter = 0.1 * np.random.rand(points.shape[0], 2)
    points_jittered = points + jitter
    
    # Calculate Voronoi diagram
    vor = Voronoi(points_jittered)
    
    # Plot Voronoi diagram
    fig, ax = plt.subplots()
    voronoi_plot_2d(vor, ax=ax)
    
    return vor, ax