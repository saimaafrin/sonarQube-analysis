import numpy as np
from sklearn.decomposition import PCA
def task_func(tuples_list, n_components):
    """
    Perform Principal Component Analysis (PCA) on a list of tuples.

    Parameters:
    tuples_list (list of tuples): The input data to be transformed.
    n_components (int): The number of principal components to keep.

    Returns:
    transformed_data (ndarray): The transformed data.
    """
    # Convert the list of tuples to a numpy array
    data = np.array(tuples_list)
    
    # Initialize the PCA model with the specified number of components
    pca = PCA(n_components=n_components)
    
    # Fit the PCA model to the data and transform it
    transformed_data = pca.fit_transform(data)
    
    return transformed_data