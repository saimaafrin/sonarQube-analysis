import numpy as np
from sklearn.cluster import KMeans
def task_func(data, n_clusters):
    # Perform KMeans clustering on the data
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)

    # Get the cluster labels for each data point
    cluster_labels = kmeans.labels_

    # Create a dictionary to store the cluster labels and indices
    cluster_dict = {}

    # Loop through each data point and add it to the appropriate cluster
    for i, label in enumerate(cluster_labels):
        if label not in cluster_dict:
            cluster_dict[label] = [i]
        else:
            cluster_dict[label].append(i)

    # Sort the clusters by the first index in each cluster
    cluster_list = list(cluster_dict.values())
    cluster_list.sort(key=lambda x: x[0])

    return cluster_dict
data = np.array([[1, 1], [2, 2]])
n_clusters = 2