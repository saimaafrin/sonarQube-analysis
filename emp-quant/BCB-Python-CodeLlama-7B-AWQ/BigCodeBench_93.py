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

    # Create DataFrame with transformed data
    pca_df = pd.DataFrame(pca_data, columns=["PC{}".format(i) for i in range(1, n_components + 1)])

    # Generate scatter plot of transformed data
    fig, ax = plt.subplots()
    ax.scatter(pca_df["PC1"], pca_df["PC2"])
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    ax.set_title("Scatter Plot of Transformed Data")

    return pca_df, ax