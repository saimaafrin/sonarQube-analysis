from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
N_COMPONENTS = 2
def task_func(L):
    # Convert list of lists to 2D numeric array
    X = np.array(L)

    # Apply PCA to the data
    pca = PCA(n_components=N_COMPONENTS)
    X_pca = pca.fit_transform(X)

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(X_pca[:, 0], X_pca[:, 1], c=X[:, 0], cmap='viridis')
    ax.set_xlabel('Principal component 1')
    ax.set_ylabel('Principal component 2')
    ax.set_title('Scatter plot of PCA results')

    # Return PCA result and scatter plot
    return (X_pca, ax)
L = [[1, 2], [3, 4], [5, 6], [7, 8]]