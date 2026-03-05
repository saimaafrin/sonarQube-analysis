import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
def task_func(n_samples=100, centers=3, n_features=2, random_seed=42):
    # Generate isotropic Gaussian blobs
    X, y = make_blobs(n_samples=n_samples, centers=centers, n_features=n_features, random_state=random_seed)

    # Visualize the blobs
    fig, ax = plt.subplots()
    ax.scatter(X[:, 0], X[:, 1], c=y)
    ax.set_title('Isotropic Gaussian Blobs')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_zlabel('Label')

    return X, y, ax
n_samples = 100
centers = 3
n_features = 2
random_seed = 42