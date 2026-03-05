import pandas as pd
from sklearn.cluster import KMeans
def task_func(x_list, y_list, n_clusters=2, random_state=0):
    """
    Perform K-Means clustering on the given data by first turning it into a DataFrame with two columns "x" and "y" 
    and then return the labels and centroids.
    
    Parameters:
    x_list (list): A list of x coordinates.
    y_list (list): A list of y coordinates.
    n_clusters (int): The number of clusters to form as well as the number of centroids to generate. Default is 2.
    random_state (int): Controls the random number generation for centroid initialization. Default is 0.
    
    Returns:
    tuple: The labels and centroids as numpy arrays.
    """
    # Create a DataFrame from the provided x and y lists
    data = pd.DataFrame({'x': x_list, 'y': y_list})
    
    # Initialize and fit the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(data)
    
    # Return the labels and centroids
    return kmeans.labels_, kmeans.cluster_centers_