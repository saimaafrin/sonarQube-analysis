
from scipy.spatial.distance import cdist
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

def task_func(n_samples=200, centers=4, plot_path=None, random_seed=None):
    # Generate synthetic data
    if random_seed is not None:
        np.random.seed(random_seed)
    X, y = make_blobs(n_samples=n_samples, centers=centers, random_state=random_seed)

    # Calculate Euclidean distances
    distances = cdist(X, X, 'euclidean')

    # Visualize the dataset
    fig, ax = plt.subplots()
    scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_title('Synthetic Dataset Visualization')
    plt.colorbar(scatter)

    if plot_path is not None:
        plt.savefig(plot_path)
        plt.close()
        return None
    else:
        return distances, ax