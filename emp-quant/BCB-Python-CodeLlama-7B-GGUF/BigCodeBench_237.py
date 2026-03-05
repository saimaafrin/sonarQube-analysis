
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(data, save_plot=False, plot_path=None):
    # Check if save_plot is True but plot_path is not provided
    if save_plot and plot_path is None:
        raise ValueError("If save_plot is True, plot_path must be provided")

    # Unzip the list of objects and their 3D coordinates
    objects, coordinates = zip(*data)

    # Convert the list of coordinates to a numpy array
    coordinates = np.array(coordinates)

    # Run PCA to reduce the dimensionality to 2D
    pca = PCA(n_components=2)
    coordinates_2d = pca.fit_transform(coordinates)

    # Create a plot of the 2D coordinates
    fig, ax = plt.subplots()
    ax.scatter(coordinates_2d[:, 0], coordinates_2d[:, 1], c=objects)

    # Save the plot if requested
    if save_plot:
        fig.savefig(plot_path)
        return coordinates_2d, ax

    # Return the 2D coordinates and the plot's Axes
    return coordinates_2d, ax