import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
def task_func(arr):
    # Perform PCA on the sum of rows of the 2D numpy array
    pca = PCA(n_components=1)
    pca_sum = pca.fit_transform(arr.sum(axis=1))

    # Plot the explained variance ratio
    ax = plt.figure().add_subplot(111)
    ax.plot(pca_sum)
    ax.set_title("Explained Variance Ratio of Principal Components")
    ax.set_xlabel("Principal Component")
    ax.set_ylabel("Explained Variance Ratio")
    plt.show()

    return ax
arr = np.array([[1, 2], [3, 4], [5, 6]])