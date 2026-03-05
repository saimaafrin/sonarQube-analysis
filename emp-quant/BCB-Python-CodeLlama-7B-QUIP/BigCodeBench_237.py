
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(data, save_plot=False, plot_path=None):
    # Unzip the data
    coordinates_3d = np.array(data)
    coordinates_2d = coordinates_3d[:, :2]

    # Perform PCA on the 2D coordinates
    pca = PCA(n_components=2)
    pca_coordinates_2d = pca.fit_transform(coordinates_2d)

    if save_plot:
        # Save the plot to the provided path
        if plot_path is None:
            raise ValueError("save_plot is True but plot_path is not provided")
        fig, ax = plt.subplots()
        ax.scatter(pca_coordinates_2d[:, 0], pca_coordinates_2d[:, 1])
        fig.savefig(plot_path)
        return pca_coordinates_2d, ax
    else:
        return pca_coordinates_2d