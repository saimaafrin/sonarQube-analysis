
import pandas as pd
from sklearn.cluster import KMeans

def task_func(data, n_clusters=3, seed=None):
    # Check if the DataFrame contains only numeric values
    if not all(data.dtypes == 'float64' or data.dtypes == 'int64'):
        raise ValueError("DataFrame contains non numeric entries")
    
    # Initialize the KMeans model with the specified parameters
    kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=seed)
    
    # Fit the model to the data
    kmeans.fit(data)
    
    # Get the cluster labels for each data point
    labels = kmeans.labels_
    
    # Return the cluster labels and the fitted KMeans model
    return labels, kmeans