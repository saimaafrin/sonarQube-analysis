
import numpy as np
from sklearn.decomposition import PCA

def task_func(tuples_list, n_components):
    # Perform PCA on the tuples
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(tuples_list)
    return transformed_data