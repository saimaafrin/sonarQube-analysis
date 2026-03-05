
import numpy as np
from sklearn.cluster import KMeans

def task_func(data, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data)
    cluster_labels = kmeans.labels_
    cluster_dict = {}
    for i in range(n_clusters):
        cluster_dict[i] = np.where(cluster_labels == i)[0].tolist()
    return cluster_dict