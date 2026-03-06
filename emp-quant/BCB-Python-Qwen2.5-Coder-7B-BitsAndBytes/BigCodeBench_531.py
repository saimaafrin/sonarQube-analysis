
from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df, n_clusters=3, random_state=None, n_init=10):
    # Identify duplicate points
    duplicates = df.duplicated(keep=False)
    duplicate_points = df[duplicates].reset_index(drop=True)
    
    # Count occurrences of each duplicate point
    duplicate_counter = Counter(tuple(row) for row in duplicate_points.values)
    
    # Remove duplicates to perform KMeans on unique points
    unique_points = df.drop_duplicates()
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init).fit(unique_points[['x', 'y']])
    labels = kmeans.labels_
    
    # Add cluster information back to the original DataFrame
    df['cluster'] = labels
    
    # Plotting the clustered data
    fig, ax = plt.subplots()
    for i in range(n_clusters):
        cluster_points = df[df['cluster'] == i]
        ax.scatter(cluster_points['x'], cluster_points['y'], label=f'Cluster {i}')
    
    ax.legend()
    plt.show()
    
    return (duplicate_counter, df, ax)