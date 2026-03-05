import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df: pd.DataFrame):
    # Replace missing values with the mean of the respective column
    df.fillna(df.mean(), inplace=True)
    
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Perform PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(numeric_df)
    
    # Create a DataFrame with the principal components
    principal_df = pd.DataFrame(data=principal_components, columns=['principal component 1', 'principal component 2'])
    
    # Create a scatter plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='principal component 1', y='principal component 2', data=principal_df)
    plt.xlabel('principal component 1')
    plt.ylabel('principal component 2')
    plt.title('PCA Scatter Plot')
    
    # Return the DataFrame and the Axes object
    return principal_df, plt.gca()