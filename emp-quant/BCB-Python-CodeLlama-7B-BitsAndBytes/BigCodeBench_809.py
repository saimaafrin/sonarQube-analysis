
import numpy as np
from sklearn.cluster import KMeans

def task_func(data, n_clusters):
    # Perform KMeans clustering on the data
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data)

    # Get the cluster labels for each data point
    labels = kmeans.labels_

    # Create a dictionary to store the clusters
    clusters = {}

    # Loop through each data point and add it to the appropriate cluster
    for i, label in enumerate(labels):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(i)

    return clusters