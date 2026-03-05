import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.collections import PathCollection
def task_func(data, n_clusters=3):
    """
    Perform K-means clustering on a dataset and generate a scatter plot visualizing the clusters and their centroids.
    The function should raise the exception for:
        ValueError: If 'data' is not a pd.DataFrame.
        ValueError: If 'n_clusters' is not an integer greater than 1.
    The function should output with:
        tuple:
            np.ndarray: An array of cluster labels assigned to each sample.
            plt.Axes: An Axes object with the scatter plot showing the clusters and centroids.
    """
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
    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='o')
    ax.set_title('K-means clustering')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')

    # Return cluster labels and scatter plot
    return kmeans.labels_, ax
data = pd.DataFrame({'Feature 1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                     'Feature 2': [10, 8, 6, 4, 2, 0, -2, -4, -6, -8]})
n_clusters = 3