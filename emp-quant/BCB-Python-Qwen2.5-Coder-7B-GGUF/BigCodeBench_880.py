
import pandas as pd
from sklearn.cluster import KMeans

def task_func(data, n_clusters=3, seed=None):
    """
    Perform K-Means clustering on the given DataFrame using the sklearn KMeans algorithm.
    
    Parameters:
    - data (pd.DataFrame): DataFrame with numerical values.
    - n_clusters (int): Number of clusters to form. Default is 3.
    - seed (int): Random seed for reproducibility. Default is None.
    
    Returns:
    - labels (numpy.ndarray): Array of cluster labels.
    - model (sklearn.cluster.KMeans): Fitted KMeans model.
    
    Raises:
    - ValueError: If the DataFrame contains non-numeric entries.
    """
    # Check if the DataFrame contains only numeric values
    if not all(data.dtypes.apply(lambda x: np.issubdtype(x, np.number))):
        raise ValueError("DataFrame contains non-numeric entries.")
    
    # Initialize the KMeans model
    model = KMeans(n_clusters=n_clusters, n_init=10, random_state=seed)
    
    # Fit the model to the data
    labels = model.fit_predict(data)
    
    return labels, model