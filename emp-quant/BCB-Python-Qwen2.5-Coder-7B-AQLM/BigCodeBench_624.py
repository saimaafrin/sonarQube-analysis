
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

# Constants
N_COMPONENTS = 2

def task_func(L):
    """
    Convert a list of lists 'L' into a 2D numeric array, apply PCA to it and return the PCA result and scatter plot.
    
    Parameters:
    L (list of lists): The input list of lists to be converted and analyzed.
    
    Returns:
    tuple: A tuple containing the PCA result (numpy array) and the scatter plot (matplotlib Axes object).
    """
    # Convert the list of lists to a numpy array
    data = np.array(L)
    
    # Initialize PCA with the specified number of components
    pca = PCA(n_components=N_COMPONENTS)
    
    # Fit the PCA model to the data and transform it
    pca_result = pca.fit_transform(data)
    
    # Create a scatter plot of the PCA result
    fig, ax = plt.subplots()
    ax.scatter(pca_result[:, 0], pca_result[:, 1])
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA Scatter Plot')
    
    # Return the PCA result and the scatter plot
    return pca_result, ax