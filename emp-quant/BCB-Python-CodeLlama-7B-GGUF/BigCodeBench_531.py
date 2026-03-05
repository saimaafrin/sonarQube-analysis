
from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(df, n_clusters=3, random_state=None, n_init=10):
    # Identify duplicate points in the DataFrame
    unique_points = df.drop_duplicates()
    duplicate_points = df.duplicated()

    # Perform KMeans clustering on the unique points
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init)
    kmeans.fit(unique_points)

    # Record the clusters
    clusters = kmeans.labels_

    # Add a column to the DataFrame with the cluster assignments
    df['cluster'] = clusters

    # Plot the clustered data
    fig, ax = plt.subplots()
    ax.scatter(df['x'], df['y'], c=clusters)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Clustered Data')

    # Return the Counter object and the DataFrame with the cluster assignments
    return Counter(duplicate_points), df