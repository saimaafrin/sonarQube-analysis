
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def task_func(array: list, random_seed: int = 42) -> (pd.DataFrame, np.ndarray):
    # Convert the 2D list to a pandas DataFrame
    df = pd.DataFrame(array)
    
    # Initialize the PCA model with the specified random seed
    pca = PCA(n_components=2, random_state=random_seed)
    
    # Fit and transform the DataFrame
    pca_result = pca.fit_transform(df)
    
    # Return the original DataFrame and the transformed data as a numpy array
    return df, pca_result