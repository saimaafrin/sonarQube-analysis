
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame):
    # Perform PCA on the DataFrame
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(df.select_dtypes(include=[np.number]))

    # Replace missing values with column means
    principal_components = principal_components.fillna(principal_components.mean())

    # Create a new DataFrame with the principal components
    principal_components_df = pd.DataFrame(data=principal_components, columns=['Component 1', 'Component 2'])

    # Draw a scatter plot of the first two principal components
    sns.scatterplot(x='Component 1', y='Component 2', data=principal_components_df)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('Scatter Plot of First Two Principal Components')

    return principal_components_df, plt.gca()