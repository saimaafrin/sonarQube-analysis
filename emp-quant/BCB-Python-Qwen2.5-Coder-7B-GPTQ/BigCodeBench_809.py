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
    kmeans = KMeans(n_clusters=n_clusters)
    
    # Fit the model to the data
    kmeans.fit(data)
    
    # Get the cluster labels for each data point
    labels = kmeans.labels_
    
    # Create a dictionary to store the indices of data points in each cluster
    cluster_dict = {}
    for i in range(n_clusters):
        cluster_dict[i] = np.where(labels == i)[0].tolist()
    
    return cluster_dict
data = np.array([[1, 1], [2, 2]])