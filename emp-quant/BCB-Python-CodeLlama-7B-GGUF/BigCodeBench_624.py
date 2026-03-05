
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

# Constants
N_COMPONENTS = 2

def task_func(L):
    # Convert list of lists to 2D numeric array
    X = np.array(L)

    # Apply PCA to the data
    pca = PCA(n_components=N_COMPONENTS)
    X_pca = pca.fit_transform(X)

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(X_pca[:, 0], X_pca[:, 1], c=X[:, 2], cmap='viridis')
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA of the data')

    # Return PCA result and scatter plot
    return (X_pca, ax)