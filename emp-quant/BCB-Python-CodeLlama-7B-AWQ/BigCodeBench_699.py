import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
def task_func(x_list, y_list, n_clusters=2, random_state=0):
    """
    Perform K-Means clustering on the given data by first turning it into a DataFrame with two columns "x" and "y" and then return the labels and centroids.
    """
    # Create a DataFrame with the given data
    df = pd.DataFrame({'x': x_list, 'y': y_list})

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(df)

    # Return the labels and centroids
    return kmeans.labels_, kmeans.cluster_centers_
x_list = [1, 2, 3, 4, 5]
y_list = [2, 4, 6, 8, 10]
n_clusters = 2
random_state = 0