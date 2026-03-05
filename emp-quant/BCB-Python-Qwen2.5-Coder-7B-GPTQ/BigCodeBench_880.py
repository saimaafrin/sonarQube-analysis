import pandas as pd
from sklearn.cluster import KMeans
def task_func(data, n_clusters=3, seed=None):
    """
    Perform K-Means clustering on the given DataFrame using the sklearn KMeans algorithm.
    
    Parameters:
    - data (pd.DataFrame): DataFrame with numerical values.
    - n_clusters (int): Number of clusters to form (default is 3).
    - seed (int): Seed for random number generation (default is None).
    
    Returns:
    - numpy.ndarray: Array of cluster labels.
    - sklearn.cluster.KMeans: Fitted KMeans model.
    
    Raises:
    - ValueError: If the DataFrame contains non-numeric entries.
    """
    # Check if the DataFrame contains only numeric values
    if not all(data.dtypes.apply(lambda x: np.issubdtype(x, np.number))):
        raise ValueError("DataFrame contains non-numeric entries.")
    
    # Initialize and fit the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=seed)
    labels = kmeans.fit_predict(data)
    
    return labels, kmeans
data = pd.DataFrame({
    'a': [1, 20, 2, 22, 100],
    'b': [1, 20, 2, 22, 100]
})