
import pandas as pd
from sklearn.decomposition import PCA

def task_func(df):
    # Initialize the PCA model with 2 components
    pca = PCA(n_components=2)
    
    # Fit the PCA model to the DataFrame and transform the data
    df_pca = pca.fit_transform(df)
    
    # Convert the transformed data back into a DataFrame
    df_pca = pd.DataFrame(df_pca, columns=['PC1', 'PC2'])
    
    return df_pca