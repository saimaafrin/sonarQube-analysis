
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(l):
    # Perform PCA on the given array
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(l)

    # Plot the first two main components
    fig, ax = plt.subplots()
    ax.scatter(pca_result[:, 0], pca_result[:, 1], c=l)
    ax.set_title("PCA Result")
    ax.set_xlabel("First Principal Component")
    ax.set_ylabel("Second Principal Component")
    return ax