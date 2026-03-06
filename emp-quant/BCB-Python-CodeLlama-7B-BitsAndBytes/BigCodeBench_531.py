
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

    # Create a DataFrame with an additional column 'cluster' representing cluster assignments for unique points
    df_with_clusters = pd.concat([df, pd.DataFrame(clusters, columns=['cluster'])], axis=1)

    # Create a scatter plot of the clustered data
    fig, ax = plt.subplots()
    ax.scatter(df_with_clusters['x'], df_with_clusters['y'], c=df_with_clusters['cluster'])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Clustered Data')

    # Return a tuple containing the Counter object, the DataFrame with cluster assignments, and the scatter plot
    return Counter(duplicate_points), df_with_clusters, fig

counter, df_with_clusters, fig = task_func(df, n_clusters, random_state, n_init)

print(counter)
print(df_with_clusters)

fig.show()