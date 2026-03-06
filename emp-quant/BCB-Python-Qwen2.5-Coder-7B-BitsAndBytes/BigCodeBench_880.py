
import pandas as pd
from sklearn.cluster import KMeans

def task_func(data, n_clusters=3, seed=None):
    # Check if all columns in the DataFrame are numeric
    if not all(data.dtypes.apply(lambda x: np.issubdtype(x, np.number))):
        raise ValueError("DataFrame contains non-numeric entries.")
    
    # Initialize the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=seed)
    
    # Fit the model to the data
    kmeans.fit(data)
    
    # Get the cluster labels
    labels = kmeans.labels_
    
    return labels, kmeans