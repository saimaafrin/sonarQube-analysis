import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
def task_func(array, seed=None):
    """
    Shuffles the columns of a numpy array randomly, performs Principal Component Analysis (PCA) to reduce the dimensionality to 2 principal components, and returns these components as a pandas DataFrame.
    
    Parameters:
    array (np.ndarray): The input 2D numpy array.
    seed (int, optional): The seed for the random number generator to ensure reproducibility.
    
    Returns:
    pandas.DataFrame: DataFrame with columns 'PC1' and 'PC2' representing the two principal components.
    """
    if array.ndim != 2:
        raise ValueError("Input array must be 2D.")
    
    if array.size == 0:
        return pd.DataFrame()
    
    np.random.seed(seed)
    shuffled_array = array[:, np.random.permutation(array.shape[1])]
    
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(shuffled_array)
    
    return pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])