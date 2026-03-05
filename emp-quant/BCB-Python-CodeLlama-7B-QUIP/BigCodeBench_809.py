
import numpy as np
from sklearn.cluster import KMeans

def task_func(data, n_clusters):
    # Initialize KMeans with n_clusters clusters
    kmeans = KMeans(n_clusters=n_clusters)
    # Fit the data to the KMeans model
    kmeans.fit(data)
    # Get the cluster labels for each data point
    labels = kmeans.labels_
    # Get the indices of the data points in each cluster
    cluster_indices = kmeans.cluster_indices_
    # Create a dictionary to store the clusters and their indices
    clusters = {}
    for i in range(n_clusters):
        clusters[i] = cluster_indices[i]
    return clusters