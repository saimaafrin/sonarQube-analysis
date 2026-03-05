
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(x, y, labels):
    # Combine x and y into a single array
    data = np.vstack((x, y)).T
    
    # Initialize PCA with 2 components
    pca = PCA(n_components=2)
    
    # Fit PCA to the data
    pca.fit(data)
    
    # Transform the data using PCA
    transformed_data = pca.transform(data)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the transformed data with labels
    for label in np.unique(labels):
        indices = np.where(labels == label)
        ax.scatter(transformed_data[indices, 0], transformed_data[indices, 1], label=label)
    
    # Add legend
    ax.legend()
    
    # Set labels for the axes
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    
    # Return the figure object
    return fig