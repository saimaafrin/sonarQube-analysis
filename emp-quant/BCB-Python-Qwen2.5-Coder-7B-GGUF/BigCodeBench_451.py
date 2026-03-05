
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(n_components=2, N_SAMPLES=500, N_FEATURES=50, random_seed=None):
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate a high-dimensional dataset
    data = np.random.randn(N_SAMPLES, N_FEATURES)
    
    # Run PCA to reduce its dimensionality
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)
    
    # Calculate the covariance matrix of the transformed data
    covariance_matrix = np.cov(transformed_data, rowvar=False)
    
    # Draw a heatmap of the covariance matrix
    if n_components > 1:
        plt.figure(figsize=(8, 6))
        heatmap_axes = sns.heatmap(covariance_matrix, annot=True, fmt=".2f", cmap="YlGnBu")
        plt.title('Covariance Matrix Heatmap')
        plt.show()
    else:
        heatmap_axes = None
    
    return transformed_data, heatmap_axes