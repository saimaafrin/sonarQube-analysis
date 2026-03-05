import numpy as np
from sklearn.cluster import KMeans
def task_func(data, n_clusters=2, random_state=0):
    # Extract coordinates from the data
    coordinates = np.array([point[1:] for point in data])
    
    # Initialize and fit the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(coordinates)
    
    # Get the cluster labels
    labels = kmeans.labels_
    
    return labels
data = [('T1', 1, 1), ('T2', 1, 1.1), ('T2', 1.1, 1), ('C1', 400, 400), ('C2', 401, 401), ('B1', 35, 35)]