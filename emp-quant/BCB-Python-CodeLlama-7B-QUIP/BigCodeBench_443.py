
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(
    P: np.ndarray,
    T: np.ndarray,
    n_clusters: int = 3,
    random_state: int = 0,
    n_init: int = 10,
) -> (np.ndarray, plt.Axes):
    # Calculate the product of the matrix P and the 3D tensor T
    product = np.matmul(P, T)

    # Flatten the result
    flattened = product.flatten()

    # Apply KMeans clustering to the flattened data
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init)
    cluster_result = kmeans.fit_predict(flattened)

    # Visualize the KMeans clustering
    fig, ax = plt.subplots()
    ax.set_title("KMeans Clustering Visualization")
    ax.scatter(flattened[:, 0], flattened[:, 1], c=cluster_result)
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")
    ax.set_zlabel("Cluster")
    return cluster_result, ax