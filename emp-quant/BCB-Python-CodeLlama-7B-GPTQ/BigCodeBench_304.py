import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(df):
    # Check if the input DataFrame is empty
    if df.empty:
        return 0, 0

    # Convert the lists in the DataFrame into separate columns
    df = pd.get_dummies(df, drop_first=True)

    # Perform Principal Component Analysis (PCA)
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(df)

    # Calculate the explained variance ratio of the principal components
    explained_variance_ratio = pca.explained_variance_ratio_

    # Create a bar chart visualizing the explained variance ratio
    ax = plt.bar(range(len(explained_variance_ratio)), explained_variance_ratio)
    ax.set_xlabel("Principal Component")
    ax.set_ylabel("Explained Variance Ratio")
    ax.set_title("Explained Variance Ratio of Principal Components")

    return explained_variance_ratio, ax
df = pd.DataFrame({"dates": ["2022-01-01", "2022-01-02", "2022-01-03"],
                   "numbers": [1, 2, 3],
                   "lists": [[1, 2], [3, 4], [5, 6]]})