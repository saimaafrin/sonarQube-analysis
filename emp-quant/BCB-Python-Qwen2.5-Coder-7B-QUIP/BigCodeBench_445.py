
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

def task_func(points, seed=0):
    # Check if points is a valid numpy array
    if not isinstance(points, np.ndarray):
        raise ValueError("Input points must be a numpy array")
    
    # Check if points have the correct shape
    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError("Input points must have shape (N, 2)")
    
    # Jittering
    np.random.seed(seed)
    jitter = np.random.rand(points.shape[0], 2) * 0.1
    points += jitter
    
    # Calculate Voronoi diagram
    vor = Voronoi(points)
    
    # Plot Voronoi diagram
    fig, ax = plt.subplots()
    voronoi_plot_2d(vor, ax=ax)
    
    # Return Voronoi object and axes
    return vor, ax