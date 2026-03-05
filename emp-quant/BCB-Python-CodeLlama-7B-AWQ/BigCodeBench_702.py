import pandas as pd
from sklearn.decomposition import PCA
def task_func(df):
    """
    Perform Principal Component Analysis (PCA) on the DataFrame and record the first two main components.
    The function should output with:
        df_pca (DataFrame): The DataFrame with the first two principal components named 'PC1' and 'PC2' as columns.
    """
    # Perform PCA on the DataFrame
    pca = PCA(n_components=2)
    df_pca = pca.fit_transform(df)

    # Add the principal components as columns to the original DataFrame
    df_pca = pd.DataFrame(df_pca, columns=['PC1', 'PC2'])

    return df_pca
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': [3, 6, 9, 12, 15]})