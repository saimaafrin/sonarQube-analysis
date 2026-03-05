
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Constants for configuration
RANGE = 100
SIZE = 1000
CLUSTERS = 5

def task_func():
    # Generate random 2D points within the specified range and size
    data = np.random.rand(SIZE, 2) * RANGE

    # Apply KMeans clustering to the points
    kmeans = KMeans(n_clusters=CLUSTERS)
    kmeans.fit(data)

    # Get the cluster centroids
    centroids = kmeans.cluster_centers_

    # Plot the clustered points with each cluster displayed in a different color
    plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_, cmap='viridis')

    # Plot the centroids of the clusters
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x')

    # Add axis labels and title
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('KMeans Clustering')

    # Show the plot
    plt.show()

    # Return the data points and the fitted KMeans model
    return data, kmeans

# Run the task function
data, kmeans = task_func()