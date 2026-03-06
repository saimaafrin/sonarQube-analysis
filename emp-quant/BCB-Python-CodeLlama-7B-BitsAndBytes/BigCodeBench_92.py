
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.collections import PathCollection

def task_func(data, n_clusters=3):
    # Check if 'data' is a pd.DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("'data' must be a pd.DataFrame")

    # Check if 'n_clusters' is an integer greater than 1
    if not isinstance(n_clusters, int) or n_clusters <= 1:
        raise ValueError("'n_clusters' must be an integer greater than 1")

    # Perform K-means clustering
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data)

    # Generate scatter plot
    fig, ax = plt.subplots()
    ax.scatter(data.iloc[:, 0], data.iloc[:, 1], c=kmeans.labels_)
    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red')
    ax.set_title('K-means Clustering')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.legend()

    # Return cluster labels and scatter plot
    return kmeans.labels_, ax