
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(data, n_components=2, random_state=None):
    """
    Performs PCA on the provided dataset to reduce its dimensionality,
    and visualizes the results using a scatter plot.

    Parameters:
    - data (np.ndarray): The input dataset.
    - n_components (int): The number of principal components to keep.
    - random_state (int, optional): Seed for reproducibility.

    Returns:
    - dict: A dictionary containing:
        "transformed_data" (np.ndarray): The transformed data.
        "ax" (plt.Axes): The scatter plot visualizing the transformed data.
    """
    # Initialize PCA with the specified number of components and random state
    pca = PCA(n_components=n_components, random_state=random_state)
    
    # Fit and transform the data
    transformed_data = pca.fit_transform(data)
    
    # Create a scatter plot based on the number of components
    if n_components == 1:
        fig, ax = plt.subplots()
        ax.scatter(range(len(transformed_data)), transformed_data[:, 0], color='blue')
        ax.set_xlabel('Sample Index')
        ax.set_ylabel('Principal Component 1')
    else:
        fig, ax = plt.subplots()
        ax.scatter(transformed_data[:, 0], transformed_data[:, 1], color='blue')
        ax.set_xlabel('Principal Component 1')
        ax.set_ylabel('Principal Component 2')
    
    # Return the transformed data and the axes object
    return {
        "transformed_data": transformed_data,
        "ax": ax
    }