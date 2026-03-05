
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

def task_func(n_samples=100, centers=3, n_features=2, random_seed=42):
    """
    Create isotropic Gaussian blobs to form clusters and visualize them.

    Parameters:
    n_samples (int): The total number of points generated.
    centers (int): The number of centers to generate.
    n_features (int): The number of features for each sample.
    random_seed (int): The seed for the random number generator.

    Returns:
    tuple: A tuple containing:
        X (numpy.ndarray): The matrix of blob points.
        y (numpy.ndarray): The vector of blob labels.
        ax (matplotlib.axes.Axes): The Axes object with the scatter plot.
    """
    # Generate the isotropic Gaussian blobs
    X, y = make_blobs(n_samples=n_samples, centers=centers, n_features=n_features, random_state=random_seed)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_title('Isotropic Gaussian Blobs')
    
    # Add a colorbar to the plot
    fig.colorbar(scatter)
    
    return X, y, ax