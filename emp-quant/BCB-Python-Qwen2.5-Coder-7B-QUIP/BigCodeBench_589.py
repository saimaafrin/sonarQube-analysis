
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
# Constants for configuration
RANGE = 100
SIZE = 1000
CLUSTERS = 5

def task_func():
    # Generate random 2D points
    data_points = np.random.rand(SIZE, 2) * RANGE
    
    # Initialize and fit KMeans model
    kmeans = KMeans(n_clusters=CLUSTERS, random_state=0)
    kmeans.fit(data_points)
    
    # Get cluster centers
    centroids = kmeans.cluster_centers_
    
    # Plotting the results
    plt.scatter(data_points[:, 0], data_points[:, 1], c=kmeans.labels_, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red', s=200, alpha=0.5)
    plt.title('KMeans Clustering')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    
    # Return the data points and the fitted model
    return data_points, kmeans