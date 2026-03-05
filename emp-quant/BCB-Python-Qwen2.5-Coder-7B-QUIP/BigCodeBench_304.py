
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(df):
    if df.empty:
        return (0, 0)

    # Convert the list of numbers into separate columns
    df = df.set_index('date').T

    # Perform PCA
    pca = PCA()
    pca.fit(df)
    explained_variance_ratio = pca.explained_variance_ratio_

    # Create a bar chart for the explained variance ratio
    fig, ax = plt.subplots()
    ax.bar(range(len(explained_variance_ratio)), explained_variance_ratio, color='b')
    ax.set_title('Explained Variance Ratio of Principal Components')
    ax.set_xlabel('Principal Component')
    ax.set_ylabel('Explained Variance Ratio')

    return (explained_variance_ratio, ax)