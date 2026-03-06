
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(data, n_components=2):
    """
    Perform Principal Component Analysis (PCA) on a dataset and record the result.
    
    Parameters:
        data (pd.DataFrame): The input dataset to be analyzed.
        n_components (int): The number of principal components to keep. Must be a positive integer.
        
    Returns:
        pd.DataFrame: The transformed data with principal components.
        Axes: The matplotlib Axes object containing the scatter plot.
        
    Raises:
        ValueError: If n_components is not a positive integer.
    """
    if not isinstance(n_components, int) or n_components <= 0:
        raise ValueError("n_components must be a positive integer.")
    
    # Standardize the data
    mean = data.mean()
    std = data.std()
    standardized_data = (data - mean) / std
    
    # Perform PCA
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(standardized_data)
    
    # Create a DataFrame from the transformed data
    transformed_df = pd.DataFrame(transformed_data, columns=[f'PC{i+1}' for i in range(n_components)])
    
    # Plotting the first two principal components
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(transformed_df['PC1'], transformed_df['PC2'], alpha=0.5)
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('Scatter plot of the first two principal components')
    
    return transformed_df, ax