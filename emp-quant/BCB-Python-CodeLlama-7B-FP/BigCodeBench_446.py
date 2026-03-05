import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
def task_func(n_samples=100, centers=3, n_features=2, random_seed=42):
    """
    Create isotropic Gaussian blobs to form clusters and visualize them.

    Args:
        n_samples (int): Number of samples to generate.
        centers (int): Number of clusters.
        n_features (int): Number of features.
        random_seed (int): Random seed.

    Returns:
        tuple: A tuple containing:
            X (numpy.ndarray): The matrix of blob points.
            y (numpy.ndarray): The vector of blob labels.
            ax (matplotlib.axes.Axes): The Axes object with the scatter plot.
    """
    # Generate the blobs
    X, y = make_blobs(n_samples=n_samples, centers=centers, n_features=n_features, random_state=random_seed)

    # Visualize the blobs
    fig, ax = plt.subplots()
    ax.scatter(X[:, 0], X[:, 1], c=y)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_title('Isotropic Gaussian Blobs')

    return X, y, ax
n_samples = 100
centers = 3
n_features = 2
random_seed = 42