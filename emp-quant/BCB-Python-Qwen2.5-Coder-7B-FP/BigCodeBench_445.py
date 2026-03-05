import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
def task_func(points, seed=0):
    """
    Calculate the Voronoi diagram for a number of points in 2D and plot it.
    
    Parameters:
    - points: A numpy array of shape (n, 2) representing the points.
    - seed: An integer seed for the random number generator to ensure reproducibility.
    
    Returns:
    - tuple (vor, ax): A tuple containing:
        - vor (Voronoi): A Voronoi object representing the Voronoi diagram of the points.
        - ax (Axes): The axes of the plotted Voronoi diagram.
    """
    # Check if the input points are valid
    if not isinstance(points, np.ndarray) or points.ndim != 2 or points.shape[1] != 2:
        raise ValueError("Input points must be a numpy array of shape (n, 2).")
    
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