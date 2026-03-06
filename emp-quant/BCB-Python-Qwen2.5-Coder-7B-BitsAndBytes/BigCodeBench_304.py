
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the DataFrame is empty
    if df.empty:
        return (0, 0)

    # Convert lists in the DataFrame to separate columns
    df = pd.concat([df.drop(columns=['date']), df['numbers'].apply(pd.Series)], axis=1)

    # Initialize PCA
    pca = PCA()

    # Fit PCA on the data
    pca.fit(df)

    # Get the explained variance ratio
    explained_variance_ratio = pca.explained_variance_ratio_

    # Create a bar chart for the explained variance ratio
    fig, ax = plt.subplots()
    ax.bar(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio)
    ax.set_xlabel('Principal Component')
    ax.set_ylabel('Explained Variance Ratio')
    ax.set_title('Explained Variance Ratio of Principal Components')

    return (explained_variance_ratio, ax)