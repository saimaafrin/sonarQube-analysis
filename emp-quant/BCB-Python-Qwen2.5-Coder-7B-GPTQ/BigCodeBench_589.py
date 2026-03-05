import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
RANGE = 100
SIZE = 1000
CLUSTERS = 5
def task_func():
    # Generate random data points
    data = np.random.rand(SIZE, 2) * RANGE
    
    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=CLUSTERS, random_state=0).fit(data)
    
    # Plotting the results
    plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_, cmap='viridis')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='x')
    plt.title('KMeans Clustering')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.show()
    
    return data, kmeans