
from scipy.spatial.distance import cdist
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

def task_func(n_samples=200, centers=4, plot_path=None, random_seed=None):
    # Generate a synthetic dataset
    X, y = make_blobs(n_samples=n_samples, centers=centers, random_seed=random_seed)

    # Calculate the Euclidean distance between individual samples
    distances = cdist(X, X, metric='euclidean')

    # Plot the data
    if plot_path is not None:
        fig, ax = plt.subplots()
        ax.scatter(X[:, 0], X[:, 1], c=y)
        ax.set_xlabel('Feature 1')
        ax.set_ylabel('Feature 2')
        ax.set_title('Synthetic Dataset')
        ax.set_aspect('equal')
        fig.savefig(plot_path)
        return None
    else:
        return distances, ax