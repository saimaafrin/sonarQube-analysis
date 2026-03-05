from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def task_func(df, n_clusters=3, random_state=None, n_init=10):
    """
    Identify duplicate points in a DataFrame, perform KMeans clustering on the unique points, and record the clusters.
    The function should output with:
        tuple: A tuple containing:
            Counter: A Counter object with the count of duplicate points.
            pd.DataFrame: A DataFrame with an additional column 'cluster' representing cluster assignments for unique points.
            Axes: A scatter plot of the clustered data.
    """
    # Identify duplicate points
    df_unique = df.drop_duplicates()
    df_duplicate = df[~df.index.isin(df_unique.index)]
    duplicate_count = Counter(df_duplicate.index)

    # Perform KMeans clustering on unique points
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init)
    kmeans.fit(df_unique)
    df_unique['cluster'] = kmeans.labels_

    # Plot the clustered data
    fig, ax = plt.subplots()
    ax.scatter(df_unique['x'], df_unique['y'], c=df_unique['cluster'])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Clustered Data')

    return (duplicate_count, df_unique, ax)
df = pd.DataFrame({'x': np.random.rand(100), 'y': np.random.rand(100)})