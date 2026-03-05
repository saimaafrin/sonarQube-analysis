from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def task_func(df, n_clusters=3, random_state=None, n_init=10):
    # Identify duplicate points in the DataFrame
    unique_points = df.drop_duplicates()

    # Perform KMeans clustering on the unique points
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=n_init)
    kmeans.fit(unique_points)

    # Record the clusters
    cluster_assignments = kmeans.labels_
    unique_points['cluster'] = cluster_assignments

    # Plot the clustered data
    fig, ax = plt.subplots()
    ax.scatter(unique_points['x'], unique_points['y'], c=cluster_assignments)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Clustered Data')
    plt.show()

    # Return the results
    return (Counter(cluster_assignments), unique_points, ax)
df = pd.DataFrame({'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   'y': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})