
import pandas as pd
from sklearn.cluster import KMeans

def task_func(data, n_clusters=3, seed=None):
    # Check if the DataFrame contains only numeric values
    if not data.select_dtypes(include=['number']).equals(data):
        raise ValueError("DataFrame must contain only numeric values")
    
    # Initialize the KMeans model with the specified parameters
    kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=seed)
    
    # Fit the model to the data
    kmeans.fit(data)
    
    # Get the cluster labels for the data
    labels = kmeans.labels_
    
    # Return the labels and the fitted model
    return labels, kmeans

labels, model = task_func(data, seed=213)
print(labels)  # Output: [2 0 2 0 1]
print(model)   # Output: KMeans(n_clusters=3, n_init=10, random_state=213)