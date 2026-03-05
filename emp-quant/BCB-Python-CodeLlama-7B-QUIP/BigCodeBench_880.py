
import pandas as pd
from sklearn.cluster import KMeans

def task_func(data, n_clusters=3, seed=None):
    # Check if the input data is a Pandas DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("The input data must be a Pandas DataFrame")

    # Check if the DataFrame contains non-numeric entries
    if not data.select_dtypes(include=[np.number]).empty:
        raise ValueError("The DataFrame cannot contain non-numeric entries")

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=seed)
    kmeans.fit(data)

    # Get the cluster labels
    labels = kmeans.labels_

    return labels, kmeans