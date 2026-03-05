import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.collections import PathCollection
def task_func(data, n_clusters=3):
    # Check if 'data' is a pd.DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input 'data' must be a pandas DataFrame.")
    
    # Check if 'n_clusters' is an integer greater than 1
    if not isinstance(n_clusters, int) or n_clusters <= 1:
        raise ValueError("Input 'n_clusters' must be an integer greater than 1.")
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(data)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(data.iloc[:, 0], data.iloc[:, 1], c=cluster_labels, cmap='viridis')
    
    # Plot centroids
    centroids = kmeans.cluster_centers_
    ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='red')
    
    # Add a colorbar to the plot
    cbar = plt.colorbar(scatter)
    cbar.set_label('Cluster Label')
    
    # Return the cluster labels and the Axes object
    return cluster_labels, ax