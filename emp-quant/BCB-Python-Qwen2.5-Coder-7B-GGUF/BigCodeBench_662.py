
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(x, y, labels):
    # Combine x and y into a single array
    data = np.vstack((x, y)).T
    
    # Perform PCA
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(data)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the principal components
    ax.scatter(principalComponents[:, 0], principalComponents[:, 1], c=labels, cmap='viridis')
    
    # Add labels to the axes
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    
    # Show the plot
    plt.show()
    
    return fig