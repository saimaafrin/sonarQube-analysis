import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
RANGE = 100
SIZE = 1000
CLUSTERS = 5
def task_func():
    # Generate random 2D points within the specified range
    data = np.random.rand(SIZE, 2) * RANGE

    # Apply KMeans clustering to the points
    kmeans = KMeans(n_clusters=CLUSTERS)
    kmeans.fit(data)

    # Plot the clustered points with each cluster displayed in a different color
    plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_)

    # Plot the centroids of the clusters
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red')

    # Show the plot
    plt.show()

    # Return the data points and the fitted KMeans model
    return data, kmeans