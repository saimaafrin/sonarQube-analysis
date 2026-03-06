
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.collections import PathCollection

def task_func(data, n_clusters=3):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame.")
    
    if not isinstance(n_clusters, int) or n_clusters <= 1:
        raise ValueError("Number of clusters must be an integer greater than 1.")
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=n_clusters)
    cluster_labels = kmeans.fit_predict(data)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(data.iloc[:, 0], data.iloc[:, 1], c=cluster_labels)
    centroids = kmeans.cluster_centers_
    centroid_scatter = ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, color='red')
    
    return cluster_labels, ax