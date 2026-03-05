import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
def task_func(x, y, labels):
    """
    Perform Principal Component Analysis (PCA) on the given x and y values and record the results with labels.
    
    Parameters:
    x (np.array): The x-values for the data points.
    y (np.array): The y-values for the data points.
    labels (list): A list of labels for each data point.
    
    Returns:
    fig (matplotlib.figure.Figure): A Matplotlib figure object containing the PCA plot.
    """
    # Combine x and y into a single array
    data = np.vstack((x, y)).T
    
    # Perform PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(data)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the data points with labels
    for i, label in enumerate(labels):
        ax.scatter(principal_components[i, 0], principal_components[i, 1], label=label)
    
    # Add labels and title
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA of Data Points')
    ax.legend()
    
    return fig