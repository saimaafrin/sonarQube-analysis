
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

def task_func(array, seed=None):
    if not isinstance(array, np.ndarray):
        raise ValueError("Input array must be a numpy array.")
    if array.ndim != 2:
        raise ValueError("Input array must be 2D.")
    if seed is not None:
        np.random.seed(seed)
    shuffled_array = np.random.permutation(array)
    pca = PCA(n_components=2)
    pca.fit(shuffled_array)
    components = pd.DataFrame({"PC1": pca.components_[0], "PC2": pca.components_[1]})
    return components