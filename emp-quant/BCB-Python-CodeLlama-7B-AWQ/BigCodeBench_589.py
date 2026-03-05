import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
RANGE = 100
SIZE = 1000
CLUSTERS = 5
def task_func():
    # Generate random 2D points within the specified range and size
    data = np.random.rand(SIZE, 2) * RANGE
    # Apply KMeans clustering to the points
    kmeans = KMeans(n_clusters=CLUSTERS)
    kmeans.fit(data)
    # Plot the clustered points with each cluster displayed in a different color
    plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_)
    # Plot the centroids of the clusters highlighted
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', s=100)
    plt.show()
    return data, kmeans