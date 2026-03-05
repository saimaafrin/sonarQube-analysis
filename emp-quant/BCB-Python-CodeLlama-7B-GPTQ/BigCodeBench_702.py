import pandas as pd
from sklearn.decomposition import PCA
def task_func(df):
    # Perform PCA on the DataFrame
    pca = PCA(n_components=2)
    df_pca = pca.fit_transform(df)

    # Add the first two principal components as columns to the DataFrame
    df_pca['PC1'] = df_pca[:, 0]
    df_pca['PC2'] = df_pca[:, 1]

    return df_pca
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})