
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

def task_func(array, seed=None):
    """
    Shuffles the columns of a numpy array randomly, performs Principal Component Analysis (PCA)
    to reduce the dimensionality to 2 principal components, and returns these components as a pandas DataFrame.

    Parameters:
    - array: A 2D numpy array.
    - seed: Optional integer to set the random seed for reproducibility.

    Returns:
    - pandas.DataFrame: DataFrame with columns 'PC1' and 'PC2' representing the two principal components.
    """
    # Check if the input array is 2D
    if len(array.shape) != 2:
        raise ValueError("Input array must be 2D.")

    # Shuffle the columns of the array
    if seed is not None:
        np.random.seed(seed)
    shuffled_array = array[:, np.random.permutation(array.shape[1])]

    # Perform PCA to reduce the dimensionality to 2 principal components
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(shuffled_array)

    # Create a DataFrame with the principal components
    df_pca = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

    return df_pca