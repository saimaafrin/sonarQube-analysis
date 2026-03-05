import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(df):
    """
    Perform Principal Component Analysis (PCA) on the dataframe and visualize the two main components.

    Parameters:
    df (pd.DataFrame): The input DataFrame to perform PCA on.

    Returns:
    pd.DataFrame: A pandas DataFrame with the principal components named 'Principal Component 1' and 'Principal Component 2'.
    Axes: A Matplotlib Axes object representing the scatter plot of the two principal components.
    """
    # Check if the input is a DataFrame and is not empty
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame")

    # Perform PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(df)
    principal_df = pd.DataFrame(data=principal_components, columns=['Principal Component 1', 'Principal Component 2'])

    # Plot the PCA results
    fig, ax = plt.subplots()
    ax.scatter(principal_df['Principal Component 1'], principal_df['Principal Component 2'])
    ax.set_title('2 Component PCA')
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')

    return principal_df, ax