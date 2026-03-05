import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(data, save_plot=False, plot_path=None):
    """
    Unzip a list of objects and their 3D coordinates, run PCA to reduce the dimensionality to 2D, and depending on the value of save_plot parameter, either save the plot to the provided path and return the 2D coordinates or return the 2D coordinates and the plot's Axes.
    """
    # Check if save_plot is True but plot_path is not provided
    if save_plot and not plot_path:
        raise ValueError("If save_plot is True, plot_path must be provided")

    # Unzip the data
    x, y, z = zip(*data)

    # Create a PCA object
    pca = PCA(n_components=2)

    # Fit the PCA object to the data
    pca.fit(np.array([x, y, z]))

    # Get the 2D coordinates
    coordinates_2d = pca.transform(np.array([x, y, z]))

    # Plot the data
    fig, ax = plt.subplots()
    ax.scatter(coordinates_2d[:, 0], coordinates_2d[:, 1], c=z)

    # Save the plot if save_plot is True
    if save_plot:
        plt.savefig(plot_path)
        return coordinates_2d, ax

    # Return the 2D coordinates and the plot's Axes if save_plot is False
    return coordinates_2d, ax
data = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
]