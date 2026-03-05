import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
def task_func(data, n_components=2):
    """
    Perform Principal Component Analysis (PCA) on a dataset and record the result.
    Also, generates a scatter plot of the transformed data.

    Parameters:
    data (pd.DataFrame): The input dataset.
    n_components (int): The number of principal components to keep.

    Returns:
    pd.DataFrame: The transformed data with principal components.
    Axes: The matplotlib Axes object containing the scatter plot.
    """
    # Check if n_components is a positive integer
    if not isinstance(n_components, int) or n_components <= 0:
        raise ValueError("n_components must be a positive integer")

    # Perform PCA
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)

    # Convert transformed data to DataFrame
    transformed_df = pd.DataFrame(transformed_data, columns=[f'PC{i+1}' for i in range(n_components)])

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(transformed_df['PC1'], transformed_df['PC2'], alpha=0.5)
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA Scatter Plot')

    return transformed_df, ax