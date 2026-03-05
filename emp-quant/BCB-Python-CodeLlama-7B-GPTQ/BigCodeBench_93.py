import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
def task_func(data, n_components=2):
    """
    Perform Principal Component Analysis (PCA) on a dataset and record the result.
    Also, generates a scatter plot of the transformed data.
    The function should raise the exception for: ValueError: If n_components is not a positive integer.
    The function should output with:
        DataFrame: The transformed data with principal components.
        Axes: The matplotlib Axes object containing the scatter plot.
    """
    # Check if n_components is a positive integer
    if not isinstance(n_components, int) or n_components <= 0:
        raise ValueError("n_components must be a positive integer")

    # Perform PCA on the data
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)

    # Generate a scatter plot of the transformed data
    fig, ax = plt.subplots()
    ax.scatter(transformed_data[:, 0], transformed_data[:, 1], c=data.iloc[:, 0])
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    ax.set_title("Scatter Plot of Transformed Data")

    # Return the transformed data and the matplotlib Axes object
    return pd.DataFrame(transformed_data, columns=["Principal Component 1", "Principal Component 2"]), ax
data = pd.DataFrame({"Feature 1": [1, 2, 3, 4, 5], "Feature 2": [6, 7, 8, 9, 10]})
n_components = 2