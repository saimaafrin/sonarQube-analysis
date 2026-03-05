import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
def task_func(x, y, labels):
    """
    Perform Principal Component Analysis (PCA) on the given x and y values and record the results with labels.
    
    Parameters:
    x (np.array): The x-values.
    y (np.array): The y-values.
    labels (np.array): The labels for the data points.
    
    Returns:
    fig (matplotlib.figure.Figure): A Matplotlib figure object containing the PCA plot.
    """
    # Combine x and y into a single array
    data = np.vstack((x, y)).T
    
    # Initialize PCA with 2 components
    pca = PCA(n_components=2)
    
    # Fit PCA to the data
    pca.fit(data)
    
    # Transform the data
    transformed_data = pca.transform(data)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the transformed data with labels
    for label in np.unique(labels):
        mask = labels == label
        ax.scatter(transformed_data[mask, 0], transformed_data[mask, 1], label=label)
    
    # Add labels and title
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA of x and y values')
    ax.legend()
    
    return fig