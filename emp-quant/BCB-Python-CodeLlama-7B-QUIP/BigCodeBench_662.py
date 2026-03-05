
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(x, y, labels):
    # Perform PCA on x and y
    pca = PCA(n_components=2)
    x_pca = pca.fit_transform(x)
    y_pca = pca.transform(y)

    # Plot the results
    fig = plt.figure(figsize=(8, 6))
    plt.scatter(x_pca[:, 0], y_pca[:, 1], c=labels, cmap='viridis')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('PCA of x and y')
    plt.show()

    return fig