
import numpy as np
from sklearn.cluster import KMeans

def task_func(data, n_clusters=2, random_state=0):
    # Extract coordinates from the data
    coords = np.array([point[1:] for point in data])
    
    # Initialize and fit the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    labels = kmeans.fit_predict(coords)
    
    return labels