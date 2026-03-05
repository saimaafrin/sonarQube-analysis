
import numpy as np
from sklearn.cluster import KMeans

def task_func(data, n_clusters=2, random_state=0):
    # Initialize KMeans with the number of clusters and a random state
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)

    # Convert the data to a numpy array
    data_array = np.array(data)

    # Fit the KMeans model to the data
    kmeans.fit(data_array)

    # Get the cluster labels for each item
    labels = kmeans.labels_

    return labels