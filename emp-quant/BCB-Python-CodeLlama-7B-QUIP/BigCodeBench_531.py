
from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(df, n_clusters=3, random_state=None, n_init=10):
    # Identify duplicate points in the DataFrame
    unique_points = df.drop_duplicates()

    # Perform KMeans clustering on the unique points
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init)
    kmeans.fit(unique_points)

    # Get the cluster assignments for the unique points
    cluster_assignments = kmeans.labels_

    # Create a Counter object with the count of duplicate points
    counter = Counter(cluster_assignments)

    # Create a DataFrame with the cluster assignments
    df_cluster = pd.DataFrame(cluster_assignments, columns=['cluster'])

    # Plot the clusters
    fig, ax = plt.subplots()
    ax.scatter(df_cluster['cluster'])
    ax.set_xlabel('Cluster')
    ax.set_ylabel('Count')
    ax.set_title('Clusters')
    plt.show()

    return counter, df_cluster, fig