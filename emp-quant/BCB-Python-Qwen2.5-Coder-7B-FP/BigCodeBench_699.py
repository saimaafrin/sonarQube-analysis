import pandas as pd
from sklearn.cluster import KMeans
def task_func(x_list, y_list, n_clusters=2, random_state=0):
    """
    Perform K-Means clustering on the given data.

    Parameters:
    x_list (list): A list of x-coordinates.
    y_list (list): A list of y-coordinates.
    n_clusters (int): The number of clusters to form.
    random_state (int): The seed used by the random number generator.

    Returns:
    tuple: A tuple containing the labels and centroids as numpy arrays.
    """
    # Create a DataFrame from the input lists
    data = pd.DataFrame({'x': x_list, 'y': y_list})
    
    # Initialize and fit the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(data)
    
    # Get the labels and centroids
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    
    return labels, centroids
x_list = [1, 2, 3, 8, 9, 10]
y_list = [1, 1, 2, 8, 8, 9]