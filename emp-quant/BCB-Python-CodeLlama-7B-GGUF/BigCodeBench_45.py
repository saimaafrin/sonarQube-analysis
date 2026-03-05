
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame):
    # Exclude non-numeric columns
    numeric_columns = df.select_dtypes(include=[np.number])

    # Perform PCA on numeric columns
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(numeric_columns)

    # Create a new DataFrame with the first two principal components
    principal_components = pd.DataFrame(pca_result[:, :2], columns=['Component 1', 'Component 2'])

    # Replace missing values with column's average
    principal_components = principal_components.fillna(principal_components.mean())

    # Draw a scatter plot of the first two main components
    sns.scatterplot(x='Component 1', y='Component 2', data=principal_components)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('Scatter Plot of First Two Principal Components')

    return principal_components, plt.gca()