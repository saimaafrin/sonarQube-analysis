import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
def task_func(array, seed=None):
    """
    Shuffles the columns of a numpy array randomly, performs Principal Component Analysis (PCA) to reduce the dimensionality to 2 principal components, and returns these components as a pandas DataFrame.
    Note that: PCA reduction will default to the number of features if fewer than 2. An named but empty DataFrame is returned for arrays without features or with empty content.
    The function should raise the exception for: ValueError: If the input array is not 2D.
    The function should output with:
        pandas.DataFrame: DataFrame with columns 'PC1' and 'PC2' representing the two principal components.
    """
    if array.ndim != 2:
        raise ValueError("Input array must be 2D.")
    if array.size == 0:
        return pd.DataFrame(columns=['PC1', 'PC2'])
    if seed is not None:
        np.random.seed(seed)
    shuffled_array = np.random.permutation(array.T)
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(shuffled_array)
    return pd.DataFrame(pca_result, columns=['PC1', 'PC2'])
array = np.array([[1, 2, 3], [4, 5, 6]])