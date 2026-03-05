import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(P, T, tensor_shape=(3, 3, 3)):
    # Calculate the product of P and T
    PT = np.matmul(P, T)

    # Apply PCA to reduce the dimensionality of the result
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(PT)

    # Visualize the result
    fig, ax = plt.subplots()
    ax.scatter(pca_result[:, 0], pca_result[:, 1], c=pca_result[:, 2])
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA Result Visualization')

    return pca_result, ax
P = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
T = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
              [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
              [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])