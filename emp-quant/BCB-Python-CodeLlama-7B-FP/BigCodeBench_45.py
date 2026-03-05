import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df: pd.DataFrame):
    # Exclude non-numeric columns
    df = df.select_dtypes(include=[np.number])

    # Replace missing values with column average
    df = df.fillna(df.mean())

    # Perform PCA
    pca = PCA(n_components=2)
    pca_df = pca.fit_transform(df)

    # Create scatter plot
    sns.scatterplot(x=pca_df[:, 0], y=pca_df[:, 1], ax=plt.gca())

    # Add labels
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')

    # Return DataFrame and Axes
    return pd.DataFrame(pca_df, columns=['Component 1', 'Component 2']), plt.gca()