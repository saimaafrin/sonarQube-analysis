
from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df, n_clusters=3, random_state=None, n_init=10):
    # Remove duplicate points
    unique_points = df.drop_duplicates(subset=['x', 'y'], keep='first')
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init)
    unique_points['cluster'] = kmeans.fit_predict(unique_points[['x', 'y']])
    
    # Count the occurrences of each cluster
    cluster_counts = Counter(unique_points['cluster'])
    
    # Plot the clusters
    plt.scatter(unique_points['x'], unique_points['y'], c=unique_points['cluster'], cmap='viridis')
    plt.colorbar()
    plt.title('Clustered Data')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    
    return cluster_counts, unique_points, plt.gca()