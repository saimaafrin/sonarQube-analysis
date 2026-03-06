
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

def task_func(points, seed=0):
    # Check input type and shape
    if not isinstance(points, np.ndarray):
        raise ValueError("Input 'points' must be a numpy array.")
    if points.ndim != 2:
        raise ValueError("Input 'points' must be a 2D array.")

    # Apply jittering to the points
    jittered_points = points + np.random.normal(size=points.shape) * 0.1

    # Create a Voronoi diagram
    vor = Voronoi(jittered_points, seed=seed)

    # Plot the Voronoi diagram
    ax = voronoi_plot_2d(vor, show_points=True)

    # Return the Voronoi object and the axes object
    return vor, ax

# Plot the Voronoi diagram
plt.show()