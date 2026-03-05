
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
# Constants for configuration
RANGE = 100
SIZE = 1000
CLUSTERS = 5

def task_func():
    # Generate a set of 2D random points within a specified range and size
    data = np.random.rand(RANGE, SIZE)
    # Apply KMeans clustering to these points
    kmeans = KMeans(n_clusters=CLUSTERS)
    kmeans.fit(data)
    # Plot the results with cluster centroids
    fig, ax = plt.subplots()
    ax.scatter(data[:, 0], data[:, 1], c=kmeans.labels_, cmap=plt.cm.Spectral)
    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x')
    plt.show()
    return data, kmeans