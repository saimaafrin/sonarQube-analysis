
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

def task_func(array, seed=None):
    if not isinstance(array, np.ndarray) or array.ndim != 2:
        raise ValueError("Input array must be a 2D numpy array.")

    if array.size == 0:
        return pd.DataFrame()

    pca = PCA(n_components=2)
    pca.fit(array)
    components = pca.components_

    return pd.DataFrame({'PC1': components[:, 0], 'PC2': components[:, 1]})