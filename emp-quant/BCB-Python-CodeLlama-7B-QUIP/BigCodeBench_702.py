
import pandas as pd
from sklearn.decomposition import PCA

def task_func(df):
    pca = PCA(n_components=2)
    pca.fit(df)
    df_pca = pd.DataFrame({'PC1': pca.components_[0], 'PC2': pca.components_[1]})
    return df_pca