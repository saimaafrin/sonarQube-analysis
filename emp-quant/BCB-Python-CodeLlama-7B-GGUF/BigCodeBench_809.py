
import numpy as np
from sklearn.cluster import KMeans

def task_func(data, n_clusters):
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data)
    
    # Get the cluster labels for each data point
    labels = kmeans.labels_
    
    # Create a dictionary to store the clusters
    clusters = {}
    
    # Loop through each data point and add it to the appropriate cluster
    for i in range(len(data)):
        # Get the cluster label for this data point
        label = labels[i]
        
        # Add the data point to the cluster
        if label not in clusters:
            clusters[label] = [i]
        else:
            clusters[label].append(i)
    
    return clusters