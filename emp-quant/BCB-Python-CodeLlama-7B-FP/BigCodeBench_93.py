import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
def task_func(data, n_components=2):
    """
    Perform Principal Component Analysis (PCA) on a dataset and record the result.
    Also, generates a scatter plot of the transformed data.
    """
    # Check if n_components is a positive integer
    if not isinstance(n_components, int) or n_components <= 0:
        raise ValueError("n_components must be a positive integer")

    # Perform PCA
    pca = PCA(n_components=n_components)
    pca_data = pca.fit_transform(data)

    # Create a DataFrame with the transformed data
    pca_data_df = pd.DataFrame(pca_data, columns=["PC{}".format(i) for i in range(1, n_components + 1)])

    # Generate a scatter plot of the transformed data
    fig, ax = plt.subplots()
    ax.scatter(pca_data_df["PC1"], pca_data_df["PC2"], c=pca_data_df["PC3"])
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    ax.set_zlabel("Principal Component 3")
    ax.set_title("Scatter Plot of Transformed Data")

    return pca_data_df, ax
data = pd.DataFrame({"Feature 1": [1, 2, 3, 4, 5], "Feature 2": [2, 4, 6, 8, 10], "Feature 3": [3, 6, 9, 12, 15]})
n_components = 3