
import numpy as np
from sklearn.cluster import KMeans

def task_func(data, n_clusters=2, random_state=0):
    # Convert the data to a numpy array
    data_array = np.array(data)

    # Apply KMeans clustering to the data
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(data_array)

    # Return the cluster labels
    return kmeans.labels_