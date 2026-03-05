import numpy as np
from sklearn.cluster import KMeans
def task_func(data, n_clusters):
    """
    Apply KMeans clustering to a 2D numeric array and find the indices of the data points in each cluster.
    """
    # Initialize KMeans
    kmeans = KMeans(n_clusters=n_clusters)

    # Fit the data to the KMeans model
    kmeans.fit(data)

    # Get the cluster labels
    cluster_labels = kmeans.labels_

    # Create a dictionary to store the cluster labels and their corresponding indices
    cluster_dict = {}

    # Loop through each data point and its corresponding cluster label
    for i, label in enumerate(cluster_labels):
        # If the cluster label is not in the dictionary, create a new list for it
        if label not in cluster_dict:
            cluster_dict[label] = []

        # Add the index of the data point to the list for its corresponding cluster label
        cluster_dict[label].append(i)

    return cluster_dict
data = np.array([[1, 1], [2, 2]])
n_clusters = 2