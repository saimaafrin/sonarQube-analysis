import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(P, T, tensor_shape=(3, 3, 3)):
    """
    Calculate the product of a matrix "P" and a 3D tensor "T" with numpy and then apply PCA to reduce the dimensionality of the result. The resulting 2D data is then visualized.
    Note that: This function only accepts numpy matrices/arrays.
    The function should output with:
        pca_result (numpy.ndarray): The result of PCA of shape (N, 2), where N is the number of rows in matrix P.
        ax (matplotlib.axes.Axes): Plot of 'PCA Result Visualization', with 'Principal Component 1' on the x-axis
        and 'Principal Component 2' on the y-axis.
    """
    # Calculate the product of P and T
    result = np.matmul(P, T)

    # Apply PCA to reduce the dimensionality of the result
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(result)

    # Visualize the result
    fig, ax = plt.subplots()
    ax.scatter(pca_result[:, 0], pca_result[:, 1], c=pca_result[:, 2])
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA Result Visualization')

    return pca_result, ax
P = np.array([[1, 2], [3, 4]])
T = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])