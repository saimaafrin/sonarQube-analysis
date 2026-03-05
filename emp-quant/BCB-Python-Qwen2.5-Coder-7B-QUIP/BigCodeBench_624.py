
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
# Constants
N_COMPONENTS = 2

def task_func(L):
    # Convert the list of lists to a 2D numpy array
    data = np.array(L)
    
    # Initialize the PCA model with the specified number of components
    pca = PCA(n_components=N_COMPONENTS)
    
    # Fit the PCA model to the data
    pca.fit(data)
    
    # Transform the data using the fitted PCA model
    pca_result = pca.transform(data)
    
    # Create a scatter plot of the PCA result
    fig, ax = plt.subplots()
    ax.scatter(pca_result[:, 0], pca_result[:, 1])
    ax.set_xlabel('First Principal Component')
    ax.set_ylabel('Second Principal Component')
    
    # Return the PCA result and the scatter plot
    return pca_result, ax