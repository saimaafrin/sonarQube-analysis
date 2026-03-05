
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.collections import PathCollection

def task_func(data, n_clusters=3):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("'data' must be a pd.DataFrame")
    if not isinstance(n_clusters, int) or n_clusters <= 1:
        raise ValueError("'n_clusters' must be an integer greater than 1")

    # Perform K-means clustering
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data)

    # Get the cluster labels and centroids
    labels = kmeans.labels_
    centroids = kmeans.centroids_

    # Create a scatter plot of the clusters and centroids
    fig, ax = plt.subplots()
    ax.scatter(data[labels == 0][0], data[labels == 0][1], color='red')
    ax.scatter(data[labels == 1][0], data[labels == 1][1], color='blue')
    ax.scatter(centroids[0], centroids[1], color='black', marker='o')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_title('K-means Clustering')
    plt.show()

    return (labels, ax)