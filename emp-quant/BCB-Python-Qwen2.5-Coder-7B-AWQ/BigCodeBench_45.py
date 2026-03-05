import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df: pd.DataFrame):
    # Drop non-numeric columns
    df_numeric = df.select_dtypes(include=[np.number])
    
    # Replace missing values with the column's average
    df_numeric.fillna(df_numeric.mean(), inplace=True)
    
    # Perform PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(df_numeric)
    
    # Create a DataFrame with the principal components
    principal_df = pd.DataFrame(data=principal_components, columns=['Component 1', 'Component 2'])
    
    # Create a scatter plot
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(principal_df['Component 1'], principal_df['Component 2'], alpha=0.5)
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    plt.title('PCA Scatter Plot')
    
    return principal_df, plt.gca()