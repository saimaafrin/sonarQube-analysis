import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def task_func(df1, df2, column1="feature1", column2="feature2"):
    """
    Merge datasets, perform KMeans clustering, then return cluster labels and scatterplot.
    Each dataset is assumed to contain at least one id column and one feature column.
    The column to process is specified for df1 and df2 via column1 and column2, respectively.
    KMeans clustering is applied with k=2 and n_init=10.
    Resulting scatterplot shows column1 on the x-axis, column2 on the y-axis, and predicted cluster as color.
    """
    # Merge datasets
    df = pd.concat([df1, df2], axis=0, ignore_index=True)

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=2, n_init=10)
    kmeans.fit(df[column1])

    # Get cluster labels
    labels = kmeans.labels_

    # Plot scatterplot
    fig, ax = plt.subplots()
    ax.scatter(df[column1], df[column2], c=labels)
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.set_title("Clustered Scatterplot")

    return labels, ax
df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1, 2, 3], "feature2": [4, 5, 6]})
df2 = pd.DataFrame({"id": [4, 5, 6], "feature1": [7, 8, 9], "feature2": [10, 11, 12]})