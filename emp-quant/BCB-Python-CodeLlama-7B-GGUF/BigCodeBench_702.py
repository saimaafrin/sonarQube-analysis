
import pandas as pd
from sklearn.decomposition import PCA

def task_func(df):
    # Perform PCA on the DataFrame
    pca = PCA(n_components=2)
    df_pca = pca.fit_transform(df)

    # Rename the first two principal components as 'PC1' and 'PC2'
    df_pca.columns = ['PC1', 'PC2']

    return df_pca