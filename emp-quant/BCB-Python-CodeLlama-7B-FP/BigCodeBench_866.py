import numpy as np
from sklearn.cluster import KMeans
def task_func(data, n_clusters=2, random_state=0):
    """
    Performs KMeans clustering on a list of data points with 2D coordinates and returns the cluster labels.
    The function takes a list of tuples, each containing an identifier and its 2D coordinates.
    It applies KMeans clustering to categorize the points.
    """
    # Convert the data to a numpy array
    data_array = np.array(data)

    # Extract the coordinates from the data array
    coordinates = data_array[:, 1:]

    # Create a KMeans object with the specified number of clusters
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)

    # Fit the KMeans object to the coordinates
    kmeans.fit(coordinates)

    # Get the cluster labels for each point
    labels = kmeans.labels_

    return labels
data = [('T1', 1, 1), ('T2', 1, 1.1), ('T2', 1.1, 1), ('C1', 400, 400), ('C2', 401, 401), ('B1', 35, 35)]