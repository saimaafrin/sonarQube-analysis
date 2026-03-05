
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input DataFrame is empty
    if df.empty:
        return 0, 0

    # Convert the lists in the DataFrame to separate columns
    df = pd.DataFrame(df.values.tolist(), index=df.index)

    # Perform PCA on the DataFrame
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(df)

    # Calculate the explained variance ratio of the principal components
    explained_variance_ratio = pca.explained_variance_ratio_

    # Create a bar chart of the explained variance ratio
    fig, ax = plt.subplots()
    ax.bar(range(len(explained_variance_ratio)), explained_variance_ratio)
    ax.set_title("Explained Variance Ratio of Principal Components")
    ax.set_xlabel("Principal Component")
    ax.set_ylabel("Explained Variance Ratio")

    return explained_variance_ratio, ax