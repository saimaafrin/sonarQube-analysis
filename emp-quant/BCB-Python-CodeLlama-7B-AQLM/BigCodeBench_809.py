import numpy as np
from sklearn.cluster import KMeans
def task_func(data, n_clusters):
    """
    Apply KMeans clustering to a 2D numeric array and find the indices of the data points in each cluster.

    Parameters:
    data (numpy array): The 2D numpy array for clustering.
    n_clusters (int): The number of clusters to form.

    Returns:
    dict: A dictionary where keys are cluster labels and values are lists of indices for data points in the cluster.

    Requirements:
    - numpy
    - sklearn.cluster

    Example:
    >>> data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    >>> cluster = task_func(data, 2)
    >>> cluster_list = list(cluster.values())
    >>> cluster_list.sort(key=lambda x: x[0])
    >>> print(cluster_list)
    [array([0, 1]), array([2, 3])]

    >>> data = np.array([[1, 1], [2, 2]])
    >>> cluster = task_func(data, 2)
    >>> cluster_list = list(cluster.values())
    >>> cluster_list.sort(key=lambda x: x[0])
    >>> print(cluster_list)
    [array([0]), array([1])]
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)
    cluster_labels = kmeans.labels_
    cluster_dict = {}
    for i in range(n_clusters):
        cluster_dict[i] = np.where(cluster_labels == i)[0]
    return cluster_dict