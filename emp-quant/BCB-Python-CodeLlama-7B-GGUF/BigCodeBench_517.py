
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def task_func(array: list, random_seed: int = 42) -> (pd.DataFrame, np.ndarray):
    # Create a DataFrame from the 2D list
    df = pd.DataFrame(array)
    
    # Apply PCA to reduce the dimensionality of the data
    pca = PCA(n_components=2, random_state=random_seed)
    pca_df = pca.fit_transform(df)
    
    # Return the original data and the PCA-transformed data
    return df, pca_df