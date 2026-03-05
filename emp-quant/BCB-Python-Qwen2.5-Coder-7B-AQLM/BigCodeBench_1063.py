
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

def task_func(arr):
    """
    Performs Principal Component Analysis (PCA) on the sum of rows of a 2D numpy array and plots the explained variance ratio.
    
    Parameters:
    arr (numpy.ndarray): A 2D numpy array.
    
    Returns:
    ax (matplotlib.axes.Axes): An Axes object from matplotlib.
    """
    # Sum the rows of the array
    summed_arr = arr.sum(axis=0)
    
    # Reshape the array to be a 2D array with a single row
    summed_arr = summed_arr.reshape(1, -1)
    
    # Perform PCA
    pca = PCA(n_components=1)
    pca.fit(summed_arr)
    
    # Get the explained variance ratio
    explained_variance_ratio = pca.explained_variance_ratio_
    
    # Plot the explained variance ratio
    fig, ax = plt.subplots()
    ax.bar(range(1), explained_variance_ratio, color='blue')
    ax.set_title('Explained Variance Ratio of Principal Components')
    ax.set_xlabel('Principal Component')
    ax.set_ylabel('Explained Variance Ratio')
    
    return ax