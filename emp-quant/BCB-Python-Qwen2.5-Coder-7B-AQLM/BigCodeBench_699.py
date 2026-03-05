
import pandas as pd
from sklearn.cluster import KMeans

def task_func(x_list, y_list, n_clusters=2, random_state=0):
    # Create a DataFrame from the provided x and y lists
    data = pd.DataFrame({'x': x_list, 'y': y_list})
    
    # Initialize the KMeans model with the specified number of clusters and random state
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    
    # Fit the KMeans model to the data
    kmeans.fit(data)
    
    # Get the labels and centroids
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    
    # Return the labels and centroids as numpy arrays
    return labels, centroids