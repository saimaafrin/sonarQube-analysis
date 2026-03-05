
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

def task_func(array, seed=None):
    if len(array.shape) != 2:
        raise ValueError("Input array must be 2D")
    
    # Shuffle columns
    np.random.seed(seed)
    col_indices = np.random.permutation(array.shape[1])
    array = array[:, col_indices]
    
    # Perform PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(array)
    
    # Convert to DataFrame
    df = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])
    
    return df