
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(s1, s2, n_clusters=3):
    if not isinstance(s1, pd.Series) or not isinstance(s2, pd.Series):
        raise ValueError("s1 and s2 must be pandas Series")
    if len(s1) != len(s2):
        raise ValueError("s1 and s2 must have the same length")
    # Perform K-Means clustering on the combined data points from s1 and s2
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(s1.values + s2.values)
    # Create a scatter plot where each cluster is visualized with a different color
    fig, ax = plt.subplots()
    ax.scatter(s1.values, s2.values, c=kmeans.labels_, cmap=plt.get_cmap(n_clusters))
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")
    ax.set_title("K-Means Clustering")
    # Add a legend to the plot
    ax.legend(kmeans.labels_, loc='best')
    return kmeans.labels_, ax