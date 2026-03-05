
import pandas as pd
from sklearn.cluster import KMeans

def task_func(data, n_clusters=3, seed=None):
    # Check if the DataFrame contains non-numeric entries
    if not data.select_dtypes(include=[np.number]).empty:
        raise ValueError("DataFrame contains non-numeric entries")

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=seed)
    labels = kmeans.fit_predict(data)

    # Return the cluster labels and the fitted KMeans model
    return labels, kmeans