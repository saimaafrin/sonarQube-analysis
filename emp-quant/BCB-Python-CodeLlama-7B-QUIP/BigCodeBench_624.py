
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
# Constants
N_COMPONENTS = 2
def task_func(L):
    # Convert list of lists to 2D array
    X = np.array(L)
    # Perform PCA
    pca = PCA(n_components=N_COMPONENTS)
    pca_result = pca.fit_transform(X)
    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(pca_result[:, 0], pca_result[:, 1])
    ax.set_xlabel('Principal component 1')
    ax.set_ylabel('Principal component 2')
    ax.set_title('PCA of list of lists')
    return (pca_result, fig)