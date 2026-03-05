import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
def task_func(data, n_components=2):
    """
    Perform Principal Component Analysis (PCA) on a dataset and record the result. Also, generates a scatter plot of the transformed data.
    
    Parameters:
    - data: A pandas DataFrame containing the dataset.
    - n_components: An integer specifying the number of principal components to keep. Must be a positive integer.
    
    Returns:
    - DataFrame: The transformed data with principal components.
    - Axes: The matplotlib Axes object containing the scatter plot.
    
    Raises:
    - ValueError: If n_components is not a positive integer.
    """
    # Check if n_components is a positive integer
    if not isinstance(n_components, int) or n_components <= 0:
        raise ValueError("n_components must be a positive integer.")
    
    # Initialize PCA
    pca = PCA(n_components=n_components)
    
    # Fit PCA and transform the data
    transformed_data = pca.fit_transform(data)
    
    # Convert the transformed data to a DataFrame
    transformed_df = pd.DataFrame(transformed_data, columns=[f'PC{i+1}' for i in range(n_components)])
    
    # Create a scatter plot of the transformed data
    fig, ax = plt.subplots()
    ax.scatter(transformed_df.iloc[:, 0], transformed_df.iloc[:, 1], alpha=0.5)
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA Scatter Plot')
    
    return transformed_df, ax