
import numpy as np
from sklearn.cluster import KMeans

def task_func(data, n_clusters=2, random_state=0):
    # Extract the coordinates from the data
    coordinates = np.array([point[1:] for point in data])
    
    # Initialize the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    
    # Fit the model to the coordinates
    labels = kmeans.fit_predict(coordinates)
    
    return labels