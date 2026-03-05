import pandas as pd
from sklearn.cluster import KMeans
def task_func(x_list, y_list, n_clusters=2, random_state=0):
    # Create a DataFrame from the given x and y lists
    data = pd.DataFrame({'x': x_list, 'y': y_list})
    
    # Initialize the KMeans model with the specified number of clusters and random state
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    
    # Fit the model to the data and predict the labels
    labels = kmeans.fit_predict(data)
    
    # Retrieve the cluster centers
    centroids = kmeans.cluster_centers_
    
    # Return the labels and centroids as numpy arrays
    return labels, centroids