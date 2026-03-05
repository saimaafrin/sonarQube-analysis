
import numpy as np
from sklearn.cluster import KMeans

def task_func(data, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)
    cluster_indices = {}
    for i in range(n_clusters):
        cluster_indices[i] = np.where(kmeans.labels_ == i)[0]
    return cluster_indices