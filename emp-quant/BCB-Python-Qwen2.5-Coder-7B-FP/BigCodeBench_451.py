import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(n_components=2, N_SAMPLES=500, N_FEATURES=50, random_seed=None):
    """
    Generate a high-dimensional dataset, run PCA to reduce its dimensionality,
    and then draw a heatmap of the covariance matrix of the transformed data.

    Parameters:
    n_components (int): The number of principal components to keep.
    N_SAMPLES (int): The number of samples in the dataset.
    N_FEATURES (int): The number of features in the dataset.
    random_seed (int): Seed for random number generation for reproducibility.

    Returns:
    tuple:
    transformed_data (ndarray): The transformed data of shape (N_SAMPLES, n_components).
    heatmap_axes (Axes): The heatmap of the covariance matrix of the transformed data or None if n_components=1.
    """
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)

    # Generate a high-dimensional dataset
    X = np.random.rand(N_SAMPLES, N_FEATURES)

    # Run PCA to reduce the dimensionality
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(X)

    # Calculate the covariance matrix of the transformed data
    covariance_matrix = np.cov(transformed_data, rowvar=False)

    # Draw a heatmap of the covariance matrix
    if n_components > 1:
        heatmap_axes = sns.heatmap(covariance_matrix, annot=True, cmap='coolwarm')
    else:
        heatmap_axes = None

    return transformed_data, heatmap_axes