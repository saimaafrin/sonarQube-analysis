
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame):
    # Replace missing values with column's average
    df = df.fillna(df.mean())

    # Perform PCA
    pca = PCA(n_components=2)
    pca_df = pca.fit_transform(df)

    # Create DataFrame with principal components
    principal_components = pd.DataFrame(pca_df, columns=['Component 1', 'Component 2'])

    # Create scatter plot
    fig, ax = plt.subplots()
    sns.scatterplot(x='Component 1', y='Component 2', data=principal_components, ax=ax)
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('PCA Scatter Plot')

    return principal_components, ax