
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(n_components=2, N_SAMPLES=500, N_FEATURES=50, random_seed=None):
    # Generate a high-dimensional dataset
    if random_seed is not None:
        np.random.seed(random_seed)
    X = np.random.rand(N_SAMPLES, N_FEATURES)

    # Run PCA to reduce dimensionality
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X)

    # Compute the covariance matrix of the transformed data
    cov_matrix = np.cov(X_pca.T)

    # Draw a heatmap of the covariance matrix
    heatmap_axes = sns.heatmap(cov_matrix, annot=True, cmap="coolwarm")

    return X_pca, heatmap_axes