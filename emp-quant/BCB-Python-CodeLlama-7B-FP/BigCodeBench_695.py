import numpy as np
from sklearn.decomposition import PCA
def task_func(tuples_list, n_components):
    """
    Perform Principal Component Analysis (PCA) on a list of tuples.

    Args:
        tuples_list (list): List of tuples to be transformed.
        n_components (int): Number of principal components to retain.

    Returns:
        transformed_data (ndarray): The transformed data.
    """
    # Convert the list of tuples to a 2D numpy array
    data = np.array(tuples_list)

    # Perform PCA on the data
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)

    return transformed_data
tuples_list = [
    (1, 2),
    (3, 4),
    (5, 6),
    (7, 8),
    (9, 10),
]
n_components = 2