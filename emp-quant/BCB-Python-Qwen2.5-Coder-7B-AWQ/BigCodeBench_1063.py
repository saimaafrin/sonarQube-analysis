from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
def task_func(arr):
    """
    Performs PCA on the sum of rows of a 2D numpy array and plots the explained variance ratio.
    
    Parameters:
    arr (numpy.ndarray): A 2D numpy array.
    
    Returns:
    ax (matplotlib.axes.Axes): An Axes object from matplotlib.
    """
    # Sum of rows
    row_sum = arr.sum(axis=1)
    
    # Reshape to 2D array with a single feature
    row_sum = row_sum.reshape(-1, 1)
    
    # Perform PCA
    pca = PCA(n_components=1)
    pca.fit(row_sum)
    
    # Plot the explained variance ratio
    fig, ax = plt.subplots()
    ax.bar(range(1, 2), pca.explained_variance_ratio_)
    ax.set_title("Explained Variance Ratio of Principal Components")
    
    return ax