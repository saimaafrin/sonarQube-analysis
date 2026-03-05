
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(n_components=2, N_SAMPLES=500, N_FEATURES=50, random_seed=None):
    # Generate a high-dimensional dataset
    np.random.seed(random_seed)
    data = np.random.rand(N_SAMPLES, N_FEATURES)

    # Run PCA to reduce the dimensionality of the data
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)

    # Create a heatmap of the covariance matrix of the transformed data
    if n_components > 1:
        cov_matrix = np.cov(transformed_data)
        heatmap_axes = sns.heatmap(cov_matrix, cmap="viridis")
    else:
        heatmap_axes = None

    return transformed_data, heatmap_axes