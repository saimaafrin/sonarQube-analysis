
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(n_components=2, N_SAMPLES=500, N_FEATURES=50, random_seed=None):
    # Generate a high-dimensional dataset
    np.random.seed(random_seed)
    X = np.random.rand(N_SAMPLES, N_FEATURES)

    # Run PCA to reduce dimensionality
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X)

    # Draw a heatmap of the covariance matrix of the transformed data
    cov_matrix = pca.components_.T @ pca.components_
    heatmap_axes = sns.heatmap(cov_matrix, annot=True, cmap="coolwarm")

    return X_pca, heatmap_axes