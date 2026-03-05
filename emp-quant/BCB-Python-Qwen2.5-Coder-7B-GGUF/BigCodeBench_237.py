
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(data, save_plot=False, plot_path=None):
    """
    Unzip a list of objects and their 3D coordinates, run PCA to reduce the dimensionality to 2D,
    and depending on the value of save_plot parameter, either save the plot to the provided path
    and return the 2D coordinates or return the 2D coordinates and the plot's Axes.
    
    Parameters:
    data (list of tuples): A list where each tuple contains an object name and its 3D coordinates (x, y, z).
    save_plot (bool): If True, save the plot to the provided path and return the 2D coordinates.
    plot_path (str, optional): The path where the plot should be saved if save_plot is True.
    
    Returns:
    coordinates_2d (numpy.ndarray): The 2D coordinates after applying PCA.
    ax (matplotlib.axes._axes.Axes, optional): The plot's Axes if save_plot is True.
    
    Raises:
    ValueError: If save_plot is True but plot_path is not provided.
    """
    # Extract coordinates from the data
    coordinates = np.array([coord for _, coord in data])
    
    # Apply PCA to reduce dimensionality to 2D
    pca = PCA(n_components=2)
    coordinates_2d = pca.fit_transform(coordinates)
    
    # Plotting
    fig, ax = plt.subplots()
    ax.scatter(coordinates_2d[:, 0], coordinates_2d[:, 1])
    for label, (x, y) in zip([obj for obj, _ in data], coordinates_2d):
        ax.annotate(label, (x, y))
    
    if save_plot:
        if plot_path is None:
            raise ValueError("plot_path must be provided if save_plot is True")
        plt.savefig(plot_path)
        plt.close()
        return coordinates_2d
    else:
        return coordinates_2d, ax