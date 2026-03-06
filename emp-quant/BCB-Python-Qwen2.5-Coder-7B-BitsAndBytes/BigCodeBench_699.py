
import pandas as pd
from sklearn.cluster import KMeans

def task_func(x_list, y_list, n_clusters=2, random_state=0):
    # Create a DataFrame from the input lists
    df = pd.DataFrame({'x': x_list, 'y': y_list})
    
    # Initialize the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    
    # Fit the model to the data
    kmeans.fit(df[['x', 'y']])
    
    # Get the labels and centroids
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    
    return labels, centroids