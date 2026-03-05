
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the DataFrame is empty
    if df.empty:
        return 0, 0

    # Convert the lists to separate columns
    df = df.melt()

    # Perform PCA
    pca = PCA(n_components=1)
    pca.fit(df)

    # Get the explained variance ratio of the principal components
    explained_variance_ratio = pca.explained_variance_ratio_

    # Plot the variance ratio bar chart
    fig, ax = plt.subplots()
    ax.bar(x=range(1), height=explained_variance_ratio, label="Explained Variance Ratio of Principal Components")
    ax.set_xlabel("Principal Component")
    ax.set_ylabel("Explained Variance Ratio")
    ax.set_title("Explained Variance Ratio of Principal Components")
    plt.show()

    return explained_variance_ratio, ax