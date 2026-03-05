
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(x, y, labels):
    # Reshape the data to be a 2D array
    data = np.vstack([x, y]).T
    
    # Initialize the PCA model
    pca = PCA(n_components=2)
    
    # Fit and transform the data
    X_pca = pca.fit_transform(data)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the data
    for i, label in enumerate(labels):
        ax.scatter(X_pca[i, 0], X_pca[i, 1], label=label)
    
    # Add a legend
    ax.legend()
    
    # Return the figure
    return fig