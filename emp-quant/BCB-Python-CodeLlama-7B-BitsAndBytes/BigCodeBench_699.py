
import pandas as pd
from sklearn.cluster import KMeans

def task_func(x_list, y_list, n_clusters=2, random_state=0):
    # Create a DataFrame with two columns "x" and "y"
    df = pd.DataFrame({'x': x_list, 'y': y_list})

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(df)

    # Return the labels and centroids as a tuple
    return kmeans.labels_, kmeans.cluster_centers_

labels, centroids = task_func(x_list, y_list, n_clusters, random_state)
print(labels)
print(centroids)