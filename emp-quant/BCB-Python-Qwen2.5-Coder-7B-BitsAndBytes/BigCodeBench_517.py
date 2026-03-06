
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def task_func(array: list, random_seed: int = 42) -> (pd.DataFrame, np.ndarray):
    # Convert the 2D list into a pandas DataFrame
    df = pd.DataFrame(array)
    
    # Initialize the PCA model with 2 components and a fixed random seed
    pca = PCA(n_components=2, random_state=random_seed)
    
    # Fit the PCA model to the data and transform it
    transformed_data = pca.fit_transform(df)
    
    return df, transformed_data