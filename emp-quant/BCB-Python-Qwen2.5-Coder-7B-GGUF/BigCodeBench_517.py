
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def task_func(array: list, random_seed: int = 42) -> (pd.DataFrame, np.ndarray):
    """
    Converts a 2D list into a pandas DataFrame and applies PCA for dimensionality reduction.
    
    Parameters:
    - array: A 2D list of numerical data.
    - random_seed: An integer to set the random seed for reproducibility.
    
    Returns:
    - pd.DataFrame: The original data in DataFrame format.
    - np.ndarray: The data after PCA transformation.
    """
    # Convert the 2D list to a pandas DataFrame
    df = pd.DataFrame(array)
    
    # Initialize PCA with the specified random seed
    pca = PCA(n_components=2, random_state=random_seed)
    
    # Fit and transform the DataFrame
    pca_result = pca.fit_transform(df)
    
    return df, pca_result