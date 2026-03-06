
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(x, y, labels):
    """
    Perform Principal Component Analysis (PCA) on the given x and y values and record the results with labels.
    
    Parameters:
    x (np.array): 1D array of x-values.
    y (np.array): 1D array of y-values.
    labels (list): List of labels for each data point.
    
    Returns:
    fig (matplotlib.figure.Figure): A Matplotlib figure object containing the PCA plot.
    """
    # Combine x and y into a single 2D array
    data = np.vstack((x, y)).T
    
    # Initialize PCA and fit it to the data
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(data)
    
    # Create a DataFrame to store the results
    import pandas as pd
    df = pd.DataFrame(data=principalComponents, columns=['Principal Component 1', 'Principal Component 2'])
    df['Label'] = labels
    
    # Plotting
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['Principal Component 1'], df['Principal Component 2'], c=df['Label'], cmap='viridis')
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA of Data Points')
    ax.legend(handles=scatter.legend_elements(), title="Labels")
    
    return fig

    fig = task_func(x, y, labels)
    plt.show()