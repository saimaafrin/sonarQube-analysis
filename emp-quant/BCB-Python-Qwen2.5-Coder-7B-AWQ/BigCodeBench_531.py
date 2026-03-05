from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
def task_func(df, n_clusters=3, random_state=None, n_init=10):
    # Identify duplicate points
    duplicates = df.duplicated(subset=['x', 'y'], keep=False)
    duplicate_counter = Counter(df.loc[duplicates, ['x', 'y']].values.tolist())
    
    # Remove duplicates to perform clustering on unique points
    unique_df = df.drop_duplicates(subset=['x', 'y'])
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init).fit(unique_df[['x', 'y']])
    unique_df['cluster'] = kmeans.labels_
    
    # Plot the clustered data
    fig, ax = plt.subplots()
    for cluster in range(n_clusters):
        cluster_points = unique_df[unique_df['cluster'] == cluster]
        ax.scatter(cluster_points['x'], cluster_points['y'], label=f'Cluster {cluster}')
    ax.legend()
    
    return duplicate_counter, unique_df, ax