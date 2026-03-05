
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.collections import PathCollection

def task_func(data, n_clusters=3):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input 'data' must be a pandas DataFrame.")
    if not isinstance(n_clusters, int) or n_clusters <= 1:
        raise ValueError("Input 'n_clusters' must be an integer greater than 1.")
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(data)
    
    fig, ax = plt.subplots()
    scatter = ax.scatter(data.iloc[:, 0], data.iloc[:, 1], c=cluster_labels, cmap='viridis')
    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X')
    
    return cluster_labels, ax