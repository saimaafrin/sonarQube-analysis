
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
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('Principal Component Analysis')
    plt.show()

    return fig

fig = task_func(x, y, labels)