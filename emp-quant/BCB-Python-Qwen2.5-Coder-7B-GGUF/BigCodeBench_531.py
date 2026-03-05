
from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df, n_clusters=3, random_state=None, n_init=10):
    # Identify duplicate points
    duplicates = df.duplicated(subset=['x', 'y'], keep=False)
    duplicate_points = df[duplicates]
    duplicate_counter = Counter(duplicate_points.groupby(['x', 'y']).size())

    # Remove duplicates to perform KMeans clustering
    unique_points = df.drop_duplicates(subset=['x', 'y'])

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init)
    unique_points['cluster'] = kmeans.fit_predict(unique_points[['x', 'y']])

    # Plot the clustered data
    fig, ax = plt.subplots()
    for cluster in unique_points['cluster'].unique():
        cluster_points = unique_points[unique_points['cluster'] == cluster]
        ax.scatter(cluster_points['x'], cluster_points['y'], label=f'Cluster {cluster}')
    ax.legend()
    plt.show()

    return duplicate_counter, unique_points, ax