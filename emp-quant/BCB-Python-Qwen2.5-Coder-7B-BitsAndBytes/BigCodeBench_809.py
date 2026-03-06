
import numpy as np
from sklearn.cluster import KMeans

def task_func(data, n_clusters):
    # Initialize the KMeans model
    kmeans = KMeans(n_clusters=n_clusters)
    
    # Fit the model to the data
    kmeans.fit(data)
    
    # Get the labels for each data point
    labels = kmeans.labels_
    
    # Create a dictionary to store the indices of data points in each cluster
    cluster_dict = {}
    
    # Iterate over the unique labels and collect the indices
    for label in np.unique(labels):
        indices = np.where(labels == label)[0]
        cluster_dict[label] = indices
    
    return cluster_dict