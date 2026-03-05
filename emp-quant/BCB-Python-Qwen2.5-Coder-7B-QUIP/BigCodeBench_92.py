
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.collections import PathCollection

def task_func(data, n_clusters=3):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("data must be a pd.DataFrame")
    if not isinstance(n_clusters, int) or n_clusters <= 1:
        raise ValueError("n_clusters must be an integer greater than 1")

    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_

    fig, ax = plt.subplots()
    scatter = ax.scatter(data.index, labels, c=labels, cmap='viridis')
    ax.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, c='r', label='Centroids')

    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_title('K-means Clustering')
    ax.legend()

    return labels, ax