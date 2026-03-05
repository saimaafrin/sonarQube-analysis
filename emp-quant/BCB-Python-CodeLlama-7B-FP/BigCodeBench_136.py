import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(df):
    """
    Perform Principal Component Analysis (PCA) on the dataframe and visualize the two main components.
    The function should raise the exception for: ValueError: If the input is not a DataFrame, or if the DataFrame is empty.
    The function should output with:
        DataFrame: A pandas DataFrame with the principal components named 'Principal Component 1' and 'Principal Component 2'.
        Axes: A Matplotlib Axes object representing the scatter plot of the two principal components. The plot includes:
            Title: '2 Component PCA'
            X-axis label: 'Principal Component 1'
            Y-axis label: 'Principal Component 2'
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty")

    # Perform PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(df)

    # Create DataFrame with principal components
    principal_components_df = pd.DataFrame(
        principal_components,
        columns=["Principal Component 1", "Principal Component 2"]
    )

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(principal_components_df["Principal Component 1"], principal_components_df["Principal Component 2"])
    ax.set_title("2 Component PCA")
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")

    return principal_components_df, ax