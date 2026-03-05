import pandas as pd
from sklearn.cluster import KMeans
def task_func(data, n_clusters=3, seed=None):
    """
    Perform K-Means clustering on the given DataFrame using the sklearn KMeans algorithm.
    
    Parameters:
    - data: pandas DataFrame with numerical values.
    - n_clusters: int, the number of clusters to form (default is 3).
    - seed: int, random seed for reproducibility (default is None).
    
    Returns:
    - labels: numpy.ndarray of cluster labels.
    - model: sklearn.cluster.KMeans, the fitted KMeans model.
    
    Raises:
    - ValueError: If the DataFrame contains non-numeric entries.
    """
    # Check if all entries in the DataFrame are numeric
    if not all(data.dtypes.apply(lambda x: np.issubdtype(x, np.number))):
        raise ValueError("DataFrame contains non-numeric entries.")
    
    # Initialize and fit the KMeans model
    model = KMeans(n_clusters=n_clusters, n_init=10, random_state=seed)
    labels = model.fit_predict(data)
    
    return labels, model
data = pd.DataFrame({
    'a': [1, 20, 2, 22, 100],
    'b': [1, 20, 2, 22, 100]
})