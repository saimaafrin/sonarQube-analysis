
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(data, save_plot=False, plot_path=None):
    # Check if save_plot is True but plot_path is not provided
    if save_plot and not plot_path:
        raise ValueError("If save_plot is True, plot_path must be provided")

    # Unzip the list of objects and their 3D coordinates
    objects = [obj for obj, coords in data]
    coords = np.array([coords for obj, coords in data])

    # Run PCA to reduce the dimensionality to 2D
    pca = PCA(n_components=2)
    coords_2d = pca.fit_transform(coords)

    # Plot the 2D coordinates
    fig, ax = plt.subplots()
    ax.scatter(coords_2d[:, 0], coords_2d[:, 1], c=objects)
    ax.set_xlabel("Dimension 1")
    ax.set_ylabel("Dimension 2")
    ax.set_title("2D Coordinates")

    # Save the plot if save_plot is True
    if save_plot:
        fig.savefig(plot_path)
        return coords_2d, ax

    # Return the 2D coordinates and the plot's Axes if save_plot is False
    return coords_2d, ax