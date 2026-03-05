import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(data, save_plot=False, plot_path=None):
    """
    Unzip a list of objects and their 3D coordinates, run PCA to reduce the dimensionality to 2D, and depending on the value of save_plot parameter, either save the plot to the provided path and return the 2D coordinates or return the 2D coordinates and the plot's Axes.
    The function should raise the exception for: ValueError: If save_plot is True but plot_path is not provided.
    The function should output with:
        coordinates_2d (numpy.ndarray): The 2D coordinates after applying PCA.
        ax (matplotlib.axes._axes.Axes, optional): The plot's Axes if save_plot is True.
    """
    # Check if save_plot is True but plot_path is not provided
    if save_plot and not plot_path:
        raise ValueError("If save_plot is True, plot_path must be provided")

    # Unzip the data
    x, y, z = zip(*data)

    # Create a PCA object and fit the data
    pca = PCA(n_components=2)
    pca.fit(np.array([x, y, z]))

    # Get the 2D coordinates
    coordinates_2d = pca.transform(np.array([x, y, z]))

    # Plot the data
    fig, ax = plt.subplots()
    ax.scatter(coordinates_2d[:, 0], coordinates_2d[:, 1], c=z)

    # Save the plot if requested
    if save_plot:
        fig.savefig(plot_path)
        return coordinates_2d, ax

    # Return the 2D coordinates and the plot's Axes
    return coordinates_2d
data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]