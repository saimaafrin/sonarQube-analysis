
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
    shuffled_array = np.random.permutation(array.T)
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(shuffled_array)
    return pd.DataFrame(pca_result, columns=['PC1', 'PC2'])