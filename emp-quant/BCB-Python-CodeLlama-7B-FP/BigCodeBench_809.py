import numpy as np
from sklearn.cluster import KMeans
def task_func(data, n_clusters):
    """
    Apply KMeans clustering to a 2D numeric array and find the indices of the data points in each cluster.
    """
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data)

    # Get the cluster labels and indices
    cluster_labels = kmeans.labels_
    cluster_indices = kmeans.cluster_indices_

    # Create a dictionary with cluster labels as keys and lists of indices as values
    cluster_dict = {cluster_label: [] for cluster_label in set(cluster_labels)}
    for i, cluster_label in enumerate(cluster_labels):
        cluster_dict[cluster_label].append(cluster_indices[i])

    return cluster_dict
data = np.array([[1, 1], [2, 2]])
n_clusters = 2