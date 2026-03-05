import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(data, n_components=2, random_state=None):
    """
    Performs PCA on the provided dataset to reduce its dimensionality, and visualizes the results using a scatter plot.
    
    Parameters:
    - data (np.ndarray): The input dataset to be transformed.
    - n_components (int): The number of principal components to reduce the data to.
    - random_state (int, optional): Seed for the random number generator for reproducibility.
    
    Returns:
    - dict: A dictionary containing:
        "transformed_data" (np.ndarray): The transformed data.
        "ax" (plt.Axes): The scatter plot visualizing the transformed data.
    """
    # Initialize PCA with the specified number of components and random state
    pca = PCA(n_components=n_components, random_state=random_state)
    
    # Fit PCA to the data and transform it
    transformed_data = pca.fit_transform(data)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    if n_components == 1:
        ax.scatter(range(len(transformed_data)), transformed_data, color='blue')
    else:
        ax.scatter(transformed_data[:, 0], transformed_data[:, 1], color='blue')
    
    # Set labels and title
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2' if n_components > 1 else 'Value')
    ax.set_title('PCA Visualization')
    
    # Return the transformed data and the axes object
    return {"transformed_data": transformed_data, "ax": ax}