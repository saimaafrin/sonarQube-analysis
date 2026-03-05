import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(df):
    """
    Processes a DataFrame containing dates and lists of numbers. It converts the lists into separate columns, performs Principal Component Analysis (PCA), and returns the explained variance ratio of the principal components along with a bar chart visualizing this ratio. Returns 0,0 if the input DataFrame is empty.
    """
    if df.empty:
        return 0, 0

    # Convert lists to separate columns
    df = df.apply(pd.Series)

    # Perform PCA
    pca = PCA(n_components=2)
    pca_df = pca.fit_transform(df)

    # Calculate explained variance ratio
    explained_variance_ratio = pca.explained_variance_ratio_

    # Plot explained variance ratio
    fig, ax = plt.subplots()
    ax.bar(range(len(explained_variance_ratio)), explained_variance_ratio)
    ax.set_xlabel("Principal Component")
    ax.set_ylabel("Explained Variance Ratio")
    ax.set_title("Explained Variance Ratio of Principal Components")

    return explained_variance_ratio, ax
df = pd.DataFrame({"date": ["2022-01-01", "2022-01-02", "2022-01-03"], "list1": [1, 2, 3], "list2": [4, 5, 6]})