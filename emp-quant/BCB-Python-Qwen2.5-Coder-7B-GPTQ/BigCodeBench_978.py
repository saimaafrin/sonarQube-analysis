import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
def task_func(array, seed=None):
    """
    Shuffles the columns of a numpy array randomly, performs Principal Component Analysis (PCA) to reduce the dimensionality to 2 principal components, and returns these components as a pandas DataFrame.
    
    Parameters:
    array (np.ndarray): The input 2D numpy array.
    seed (int, optional): Seed for the random number generator for reproducibility. Defaults to None.
    
    Returns:
    pd.DataFrame: DataFrame with columns 'PC1' and 'PC2' representing the two principal components.
    
    Raises:
    ValueError: If the input array is not 2D.
    """
    if array.ndim != 2:
        raise ValueError("Input array must be 2D.")
    
    if array.shape[1] == 0:
        return pd.DataFrame(columns=['PC1', 'PC2'])
    
    if seed is not None:
        np.random.seed(seed)
    
    # Shuffle columns
    shuffled_array = array[:, np.random.permutation(array.shape[1])]
    
    # Perform PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(shuffled_array)
    
    # Create DataFrame
    df = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])
    
    return df