
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(data, n_components=2, random_state=None):
    """
    Performs Principal Component Analysis (PCA) on the provided dataset to reduce its dimensionality, and visualizes the results using a scatter plot.

    Parameters:
    data (np.ndarray): The input dataset to be transformed.
    n_components (int): The number of principal components to keep. Defaults to 2.
    random_state (int, optional): The seed for random number generation. Defaults to None.

    Returns:
    dict: A dictionary containing:
        "transformed_data" (np.ndarray): The transformed data.
        "ax" (plt.Axes): The scatter plot visualizing the transformed data.
    """
    # Initialize the PCA model with the specified number of components and random state
    pca = PCA(n_components=n_components, random_state=random_state)
    
    # Fit the PCA model to the data
    transformed_data = pca.fit_transform(data)
    
    # Create a scatter plot of the transformed data
    fig, ax = plt.subplots()
    if n_components == 1:
        ax.scatter(range(len(transformed_data)), transformed_data[:, 0], c='b')
    else:
        ax.scatter(transformed_data[:, 0], transformed_data[:, 1], c='b')
    
    # Set the plot title and labels
    ax.set_title(f'PCA with {n_components} Components')
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2' if n_components > 1 else 'Value')
    
    # Return the transformed data and the plot
    return {
        "transformed_data": transformed_data,
        "ax": ax
    }