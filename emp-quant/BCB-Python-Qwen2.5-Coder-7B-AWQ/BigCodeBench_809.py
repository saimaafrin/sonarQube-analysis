import numpy as np
from sklearn.cluster import KMeans
def task_func(data, n_clusters):
    """
    Apply KMeans clustering to a 2D numeric array and find the indices of the data points in each cluster.

    Parameters:
    data (np.array): A 2D numpy array of numeric data points.
    n_clusters (int): The number of clusters to form.

    Returns:
    dict: A dictionary where keys are cluster labels and values are lists of indices for data points in the cluster.
    """
    # Initialize the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    
    # Fit the model to the data
    kmeans.fit(data)
    
    # Get the cluster labels for each data point
    labels = kmeans.labels_
    
    # Create a dictionary to store the indices of data points in each cluster
    cluster_dict = {}
    for i, label in enumerate(labels):
        if label not in cluster_dict:
            cluster_dict[label] = []
        cluster_dict[label].append(i)
    
    return cluster_dict
data = np.array([[1, 1], [2, 2]])