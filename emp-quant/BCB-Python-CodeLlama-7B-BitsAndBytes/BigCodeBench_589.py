
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

    # Plot the clustered points with each cluster displayed in a different color
    plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_, cmap='viridis')

    # Plot the centroids of the clusters
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=150, linewidths=5, color='red')

    # Add labels to the plot
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('KMeans Clustering')

    # Show the plot
    plt.show()

    # Return the data points and the fitted KMeans model
    return data, kmeans

# Call the function
data, kmeans = task_func()