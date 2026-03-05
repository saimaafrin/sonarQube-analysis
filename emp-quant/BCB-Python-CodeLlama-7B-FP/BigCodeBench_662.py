import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
def task_func(x, y, labels):
    # Perform PCA on x and y
    pca = PCA(n_components=2)
    x_pca = pca.fit_transform(x)
    y_pca = pca.fit_transform(y)

    # Plot the results
    fig, ax = plt.subplots()
    ax.scatter(x_pca[:, 0], x_pca[:, 1], c=labels)
    ax.set_xlabel('Principal component 1')
    ax.set_ylabel('Principal component 2')
    ax.set_title('Principal Component Analysis')
    return fig
x = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([[7, 8], [9, 10], [11, 12]])
labels = np.array(['A', 'B', 'C'])