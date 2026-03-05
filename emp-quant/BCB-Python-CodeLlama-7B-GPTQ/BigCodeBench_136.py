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
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input must be a pandas DataFrame.")

    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")

    # Perform PCA on the DataFrame
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(df)

    # Create a DataFrame with the principal components
    principal_components_df = pd.DataFrame(principal_components, columns=["Principal Component 1", "Principal Component 2"])

    # Create a Matplotlib Axes object to visualize the principal components
    fig, ax = plt.subplots()
    ax.scatter(principal_components_df["Principal Component 1"], principal_components_df["Principal Component 2"], c="blue")
    ax.set_title("2 Component PCA")
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")

    return principal_components_df, ax
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]})