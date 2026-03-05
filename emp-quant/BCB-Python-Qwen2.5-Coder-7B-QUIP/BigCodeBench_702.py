
import pandas as pd
from sklearn.decomposition import PCA

def task_func(df):
    # Initialize the PCA model with 2 components
    pca = PCA(n_components=2)
    
    # Fit and transform the DataFrame
    df_pca = pd.DataFrame(pca.fit_transform(df), columns=['PC1', 'PC2'])
    
    return df_pca