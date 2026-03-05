
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(n_components=2, N_SAMPLES=500, N_FEATURES=50, random_seed=None):
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)

    # Generate a high-dimensional dataset
    data = np.random.randn(N_SAMPLES, N_FEATURES)

    # Run PCA to reduce the dimensionality
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)

    # Calculate the covariance matrix of the transformed data
    covariance_matrix = np.cov(transformed_data, rowvar=False)

    # Plot the heatmap of the covariance matrix
    if n_components == 1:
        heatmap_axes = None
    else:
        heatmap_axes = plt.figure().add_subplot(111)
        sns.heatmap(covariance_matrix, annot=True, cmap='viridis')
        plt.title('Covariance Matrix Heatmap')
        plt.show()

    return transformed_data, heatmap_axes