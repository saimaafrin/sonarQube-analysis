
import numpy as np
from sklearn.cluster import KMeans

def task_func(data, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)
    cluster_labels = kmeans.labels_
    cluster_indices = {}
    for i in range(n_clusters):
        cluster_indices[i] = [index for index, label in enumerate(cluster_labels) if label == i]
    return cluster_indices