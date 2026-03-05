import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df: pd.DataFrame):
    # Perform PCA on the DataFrame
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(df.select_dtypes(include=[np.number]))

    # Replace missing values with column's average
    principal_components = principal_components.fillna(principal_components.mean())

    # Create a new DataFrame with the first two principal components
    principal_components = pd.DataFrame(principal_components, columns=['Component 1', 'Component 2'])

    # Draw a scatter plot of the first two main components
    sns.scatterplot(x='Component 1', y='Component 2', data=principal_components)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('Scatter Plot of First Two Principal Components')

    # Return the DataFrame and the Axes object
    return principal_components, plt.gca()
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20]})