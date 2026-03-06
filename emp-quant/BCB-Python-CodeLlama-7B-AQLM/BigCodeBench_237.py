import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(data, save_plot=False, plot_path=None):
    """
    Unzip a list of objects and their 3D coordinates, run PCA to reduce the dimensionality to 2D, 
    and depending on the value of save_plot parameter, either save the plot to the provided path and 
    return the 2D coordinates or return the 2D coordinates and the plot's Axes.

    Parameters:
    - data (list of tuple): A list containing tuples of an object and its 3D coordinates.
    - save_plot (bool, optional): If True, the plot will be saved. Defaults to False.
    - plot_path (str, optional): The path where the plot will be saved. Required if save_plot is True.

    Returns:
    - coordinates_2d (numpy.ndarray): The 2D coordinates after applying PCA.
    - ax (matplotlib.axes._axes.Axes, optional): The plot's Axes if save_plot is True.

    Requirements:
    - numpy
    - sklearn.decomposition.PCA
    - matplotlib.pyplot

    Raises:
    - ValueError: If save_plot is True but plot_path is not provided.

    Example:
    >>> import tempfile
    >>> temp_dir = tempfile.mkdtemp()
    >>> task_func([('A', 1, 1, 1), ('B', 2, 2, 2)], save_plot=True, plot_path=f"{temp_dir}/temp_plot.png")[0]
    array([[ 8.66025404e-01,  4.09680598e-17],
           [-8.66025404e-01,  4.09680598e-17]])
    """
    coordinates = np.array([[x[1], x[2], x[3]] for x in data])
    pca = PCA(n_components=2)
    coordinates_2d = pca.fit_transform(coordinates)
    if save_plot:
        if plot_path is None:
            raise ValueError("plot_path must be provided if save_plot is True.")
        fig, ax = plt.subplots()
        ax.scatter(coordinates_2d[:, 0], coordinates_2d[:, 1], s=100, c=np.arange(len(data)))
        ax.set_xlabel("PC1")
        ax.set_ylabel("PC2")
        ax.set_title("PCA")
        fig.savefig(plot_path)
        return coordinates_2d, ax
    else:
        return coordinates_2d