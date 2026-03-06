
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

def task_func(arr):
    # Perform PCA on the sum of rows of the array
    pca = PCA(n_components=1)
    pca.fit(arr.sum(axis=1))

    # Plot the explained variance ratio
    ax = plt.gca()
    ax.plot(pca.explained_variance_ratio_)
    ax.set_title("Explained Variance Ratio of Principal Components")
    ax.set_xlabel("Principal Component")
    ax.set_ylabel("Explained Variance Ratio")
    return ax