import pandas as pd
from sklearn.decomposition import PCA
def task_func(df):
    """
    Perform Principal Component Analysis (PCA) on the DataFrame and record the first two main components.
    
    Parameters:
    df (DataFrame): The input DataFrame to perform PCA on.
    
    Returns:
    df_pca (DataFrame): The DataFrame with the first two principal components named 'PC1' and 'PC2' as columns.
    """
    # Initialize the PCA model with 2 components
    pca = PCA(n_components=2)
    
    # Fit the PCA model to the data and transform the data
    principal_components = pca.fit_transform(df)
    
    # Create a DataFrame with the principal components
    df_pca = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
    
    return df_pca