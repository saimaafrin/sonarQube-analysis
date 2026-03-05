import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df: pd.DataFrame):
    """
    Perform PCA on a DataFrame (excluding non-numeric columns) and draw a scatter plot of the first two main components. The principal columns should be name 'Component 1' and 'Component 2'. Missing values are replaced by column's average.
    The function should output with:
        DataFrame: A pandas DataFrame with the first two principal components. The columns should be 'principal component 1' and 'principal component 2'.
        Axes: A matplotlib Axes object representing the scatter plot. The xlabel should be 'principal component' and the ylabel 'principal component 2'.
    """
    # Exclude non-numeric columns
    df = df.select_dtypes(include=np.number)

    # Replace missing values with column average
    df = df.fillna(df.mean())

    # Perform PCA
    pca = PCA(n_components=2)
    pca_df = pca.fit_transform(df)

    # Create DataFrame with principal components
    principal_df = pd.DataFrame(pca_df, columns=['principal component 1', 'principal component 2'])

    # Create scatter plot
    sns.scatterplot(x='principal component 1', y='principal component 2', data=principal_df)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('Scatter Plot of First Two Principal Components')
    plt.show()

    return principal_df, plt.gca()
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': [1, 2, 3, 4, 5]})