import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
def task_func(x, y, labels):
    """
    Perform Principal Component Analysis (PCA) on the given x and y values and record the results with labels.
    
    Parameters:
    x (np.array): 1D array of x-values.
    y (np.array): 1D array of y-values.
    labels (np.array): 1D array of labels corresponding to each point.
    
    Returns:
    fig (matplotlib.figure.Figure): A Matplotlib figure object containing the PCA plot.
    """
    # Combine x and y into a single 2D array
    data = np.vstack((x, y)).T
    
    # Initialize and fit PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(data)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot each class with a different color
    unique_labels = np.unique(labels)
    colors = plt.cm.get_cmap('viridis', len(unique_labels))
    
    for label, color in zip(unique_labels, colors):
        indices = np.where(labels == label)
        ax.scatter(principal_components[indices, 0], principal_components[indices, 1], color=color, label=label)
    
    # Add labels and title
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA of x and y values')
    ax.legend()
    
    return fig