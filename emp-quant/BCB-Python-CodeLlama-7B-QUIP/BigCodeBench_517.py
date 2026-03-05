
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def task_func(array: list, random_seed: int = 42) -> (pd.DataFrame, np.ndarray):
    # Create a DataFrame from the provided 2D list
    df = pd.DataFrame(array)

    # Set a fixed random seed for reproducibility
    np.random.seed(random_seed)

    # Apply PCA to reduce the dataset to its two main components
    pca = PCA(n_components=2)
    pca_data = pca.fit_transform(df)

    return df, pca_data