import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
def task_func(array: list, random_seed: int = 42) -> (pd.DataFrame, np.ndarray):
    """
    Converts a 2D list into a pandas DataFrame and applies PCA for dimensionality reduction.
    This function creates a DataFrame from the provided 2D list and then applies PCA to reduce the dataset to its two main components.
    The function uses a fixed random seed to ensure reproducibility.
    """
    # Create a DataFrame from the provided 2D list
    df = pd.DataFrame(array)

    # Apply PCA to reduce the dataset to its two main components
    pca = PCA(n_components=2)
    pca_df = pca.fit_transform(df)

    # Return the original data in DataFrame format and the data after PCA transformation
    return df, pca_df
array = [[1, 2], [3, 4], [5, 6]]