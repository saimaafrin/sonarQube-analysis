
import pandas as pd
from sklearn.decomposition import PCA

def task_func(df):
    # Perform PCA on the DataFrame
    pca = PCA(n_components=2)
    df_pca = pca.fit_transform(df)

    # Add the principal components as columns to the original DataFrame
    df_pca = pd.concat([df, pd.DataFrame(df_pca, columns=['PC1', 'PC2'])], axis=1)

    return df_pca