import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(data, save_plot=False, plot_path=None):
    """
    Unzip a list of objects and their 3D coordinates, run PCA to reduce the dimensionality to 2D,
    and depending on the value of save_plot parameter, either save the plot to the provided path
    and return the 2D coordinates or return the 2D coordinates and the plot's Axes.
    
    Parameters:
    - data (list of tuples): A list where each tuple contains an object name and its 3D coordinates (x, y, z).
    - save_plot (bool): If True, the plot will be saved to the provided path and the function will return the 2D coordinates.
    - plot_path (str, optional): The path where the plot will be saved if save_plot is True.
    
    Returns:
    - coordinates_2d (numpy.ndarray): The 2D coordinates after applying PCA.
    - ax (matplotlib.axes._axes.Axes, optional): The plot's Axes if save_plot is True.
    
    Raises:
    - ValueError: If save_plot is True but plot_path is not provided.
    """
    # Unzip the data
    objects, coordinates = zip(*data)
    coordinates = np.array(coordinates)
    
    # Run PCA to reduce dimensionality to 2D
    pca = PCA(n_components=2)
    coordinates_2d = pca.fit_transform(coordinates)
    
    # Plotting
    if save_plot:
        if plot_path is None:
            raise ValueError("plot_path must be provided if save_plot is True")
        
        fig, ax = plt.subplots()
        ax.scatter(coordinates_2d[:, 0], coordinates_2d[:, 1], c='blue')
        ax.set_xlabel('Principal Component 1')
        ax.set_ylabel('Principal Component 2')
        ax.set_title('PCA of 3D Coordinates')
        
        plt.savefig(plot_path)
        plt.close()
        return coordinates_2d, ax
    else:
        return coordinates_2d
data = [('obj1', (1, 2, 3)), ('obj2', (4, 5, 6)), ('obj3', (7, 8, 9))]