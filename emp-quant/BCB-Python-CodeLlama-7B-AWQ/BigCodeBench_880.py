import pandas as pd
from sklearn.cluster import KMeans
def task_func(data, n_clusters=3, seed=None):
    """
    Perform K-Means clustering on the given DataFrame using the sklearn KMeans algorithm.
    The function expects a DataFrame with numerical values, as KMeans cannot handle categorical data.
    It applies standard KMeans clustering from the sklearn library to form clusters.
    The number of clusters is configurable via the 'n_clusters' parameter, defaulting to 3.
    The Number of times the k-means algorithm is run with different centroid seeds (n_init) is set to 10.
    The function returns an array of cluster labels corresponding to each data point in the input as well as the fitted KMeans model.
    """
    # Check if the DataFrame contains non-numeric entries
    if not data.select_dtypes(include=[np.number]).empty:
        raise ValueError("DataFrame contains non-numeric entries")

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=seed)
    labels = kmeans.fit_predict(data)

    # Return cluster labels and fitted KMeans model
    return labels, kmeans
data = pd.DataFrame({
    'a': [1, 20, 2, 22, 100],
    'b': [1, 20, 2, 22, 100]
})