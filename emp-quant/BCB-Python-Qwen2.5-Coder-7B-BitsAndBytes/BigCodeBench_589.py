
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Constants for configuration
RANGE = 100
SIZE = 1000
CLUSTERS = 5

def task_func():
    # Generate random data points
    data_points = np.random.rand(SIZE, 2) * RANGE
    
    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=CLUSTERS)
    kmeans.fit(data_points)
    
    # Get cluster labels and centroids
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    
    # Plotting the results
    colors = ['r', 'g', 'b', 'c', 'm']  # Colors for up to 5 clusters
    for i in range(CLUSTERS):
        cluster_points = data_points[labels == i]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], c=colors[i], label=f'Cluster {i+1}')
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='k', label='Centroids')
    plt.legend()
    plt.title('KMeans Clustering')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    
    return (data_points, kmeans)