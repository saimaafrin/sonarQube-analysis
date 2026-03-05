
import pandas as pd
from sklearn.decomposition import PCA

def task_func(df):
    # Initialize the PCA model with 2 components
    pca = PCA(n_components=2)
    
    # Fit the PCA model to the DataFrame and transform the data
    pca_result = pca.fit_transform(df)
    
    # Create a new DataFrame with the PCA results
    df_pca = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'])
    
    return df_pca