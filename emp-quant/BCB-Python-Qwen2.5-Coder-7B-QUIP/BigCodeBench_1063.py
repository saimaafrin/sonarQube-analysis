
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

def task_func(arr):
    # Ensure the input is a 2D numpy array
    if not isinstance(arr, np.ndarray) or arr.ndim != 2:
        raise ValueError("Input must be a 2D numpy array.")
    
    # Calculate the sum of rows
    row_sum = np.sum(arr, axis=1)
    
    # Perform PCA
    pca = PCA(n_components=1)
    pca.fit(row_sum.reshape(-1, 1))
    
    # Get the explained variance ratio
    explained_variance_ratio = pca.explained_variance_ratio_
    
    # Plot the explained variance ratio
    fig, ax = plt.subplots()
    ax.bar(0, explained_variance_ratio, width=0.5, color='b')
    ax.set_title('Explained Variance Ratio of Principal Components')
    ax.set_xlabel('Principal Component')
    ax.set_ylabel('Explained Variance Ratio')
    
    return ax