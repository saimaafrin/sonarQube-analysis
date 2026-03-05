
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(P, T, tensor_shape=(3, 3, 3)):
    # Calculate the product of matrix P and 3D tensor T
    P_T = np.matmul(P, T)

    # Apply PCA to reduce the dimensionality of the result
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(P_T)

    # Visualize the result
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.scatter(pca_result[:, 0], pca_result[:, 1], c='b')
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA Result Visualization')
    return pca_result, ax