import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(data, n_components=2, random_state=None):
    """
    Performs Principal Component Analysis (PCA) on the provided dataset to reduce its dimensionality, and visualizes the results using a scatter plot.

    Parameters
    ----------
    data : np.ndarray
        The dataset to be reduced.
    n_components : int, optional
        The number of principal components to retain. By default, 2.
    random_state : int, optional
        The random state to use for reproducibility. By default, None.

    Returns
    -------
    dict
        A dictionary containing:
        "transformed_data" (np.ndarray): The transformed data.
        "ax" (plt.Axes): The scatter plot visualizing the transformed data.
    """
    # Perform PCA on the data
    pca = PCA(n_components=n_components, random_state=random_state)
    transformed_data = pca.fit_transform(data)

    # Create a scatter plot of the transformed data
    fig, ax = plt.subplots()
    ax.scatter(transformed_data[:, 0], transformed_data[:, 1], c=data[:, 0], cmap="viridis")
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    ax.set_title("Scatter Plot of PCA-Transformed Data")

    return {"transformed_data": transformed_data, "ax": ax}
data = np.random.rand(100, 10)