import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(P, T, tensor_shape=(3, 3, 3)):
    # Reshape the tensor T to a 2D array
    T_reshaped = T.reshape(T.shape[0], -1)
    
    # Calculate the product of matrix P and the reshaped tensor T
    result = np.dot(P, T_reshaped)
    
    # Initialize PCA with 2 components
    pca = PCA(n_components=2)
    
    # Fit PCA to the result and transform the data
    pca_result = pca.fit_transform(result)
    
    # Create a plot for visualization
    fig, ax = plt.subplots()
    ax.scatter(pca_result[:, 0], pca_result[:, 1], alpha=0.5)
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA Result Visualization')
    
    return pca_result, ax