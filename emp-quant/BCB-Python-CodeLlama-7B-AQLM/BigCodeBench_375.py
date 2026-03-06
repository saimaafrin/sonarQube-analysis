from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(l):
    """
    Perform Principal Component Analysis (PCA) on the given array and record the first two main components.

    Parameters:
    l (numpy array): The input array.

    Returns:
    ax (matplotlib.axes._axes.Axes): Axes object of the generated plot

    Note:
    - This function use "PCA Result" as the title of the plot.
    - This function use "First Principal Component" and "Second Principal Component" as the xlabel 
    and ylabel of the plot, respectively.

    Requirements:
    - sklearn.decomposition.PCA
    - matplotlib.pyplot

    Example:
    >>> import numpy as np
    >>> l = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    >>> ax = task_func(l)
    >>> len(ax.collections[0].get_offsets())
    4
    >>> print(ax.get_title())
    PCA Result
    >>> plt.close()
    """
    pca = PCA(n_components=2)
    pca.fit(l)
    x = pca.components_[0]
    y = pca.components_[1]
    x = x * np.sqrt(pca.explained_variance_[0])
    y = y * np.sqrt(pca.explained_variance_[1])
    x = x + np.mean(l, axis=0)
    y = y + np.mean(l, axis=0)
    ax = plt.gca()
    ax.scatter(x, y)
    ax.set_title("PCA Result")
    ax.set_xlabel("First Principal Component")
    ax.set_ylabel("Second Principal Component")
    return ax