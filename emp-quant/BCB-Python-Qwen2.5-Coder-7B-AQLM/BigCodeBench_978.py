
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

def task_func(array, seed=None):
    if array.ndim != 2:
        raise ValueError("Input array must be 2D")
    
    if array.size == 0:
        return pd.DataFrame()
    
    if seed is not None:
        np.random.seed(seed)
    
    np.random.shuffle(array)
    
    pca = PCA(n_components=min(2, array.shape[1]))
    pca.fit(array)
    
    transformed = pca.transform(array)
    
    return pd.DataFrame(transformed, columns=['PC1', 'PC2'])