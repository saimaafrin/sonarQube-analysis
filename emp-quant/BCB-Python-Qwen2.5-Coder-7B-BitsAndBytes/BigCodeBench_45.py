
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame):
    # Replace missing values with the mean of each column
    df.fillna(df.mean(), inplace=True)
    
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Perform PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(numeric_df)
    
    # Create a DataFrame for the principal components
    principal_df = pd.DataFrame(data=principal_components, columns=['Principal Component 1', 'Principal Component 2'])
    
    # Plotting
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Principal Component 1', y='Principal Component 2', data=principal_df)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('PCA Scatter Plot')
    plt.show()
    
    return principal_df, plt.gca()