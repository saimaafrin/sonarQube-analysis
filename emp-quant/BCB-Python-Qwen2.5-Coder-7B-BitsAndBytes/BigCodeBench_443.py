
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
    # Calculate the product of matrix 'P' and 3D tensor 'T'
    result = np.einsum('ij,jkl->ikl', P, T)
    
    # Flatten the result
    flattened_data = result.reshape(-1, result.shape[-1])
    
    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init).fit(flattened_data)
    cluster_result = kmeans.labels_
    
    # Visualize the KMeans clustering
    fig, ax = plt.subplots()
    scatter = ax.scatter(flattened_data[:, 0], flattened_data[:, 1], c=cluster_result, cmap='viridis')
    ax.set_title('KMeans Clustering Visualization')
    plt.colorbar(scatter)
    
    return cluster_result, ax