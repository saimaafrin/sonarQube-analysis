
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

def task_func(points, seed=0):
    # Check input type and shape
    if not isinstance(points, np.ndarray):
        raise ValueError("Input must be a numpy array")
    if points.ndim != 2:
        raise ValueError("Input must be a 2D array")
    if points.shape[1] != 2:
        raise ValueError("Input must be a 2D array with 2 columns")

    # Apply jittering to the points
    np.random.seed(seed)
    points += np.random.normal(size=points.shape)

    # Create the Voronoi diagram
    vor = Voronoi(points)

    # Plot the Voronoi diagram
    ax = voronoi_plot_2d(vor, show_points=False)

    return vor, ax

# Show the plot
plt.show()