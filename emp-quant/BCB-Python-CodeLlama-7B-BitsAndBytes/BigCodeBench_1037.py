
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(s1, s2, n_clusters=3):
    # Check if s1 and s2 are pandas Series
    if not isinstance(s1, pd.Series) or not isinstance(s2, pd.Series):
        raise ValueError("s1 and s2 must be pandas Series")

    # Check if s1 and s2 have the same length
    if len(s1) != len(s2):
        raise ValueError("s1 and s2 must have the same length")

    # Combine s1 and s2 into a single pandas Series
    data = pd.concat([s1, s2], axis=1)

    # Perform K-Means clustering on the combined data
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data)

    # Create a scatter plot with each cluster colored differently
    fig, ax = plt.subplots()
    ax.scatter(data.iloc[:, 0], data.iloc[:, 1], c=kmeans.labels_)
    ax.set_title("K-Means Clustering")

    # Add a legend to the plot
    legend_elements = [Line2D([0], [0], marker='o', color=kmeans.cluster_centers_[i], label=f"Cluster {i}") for i in range(n_clusters)]
    ax.legend(handles=legend_elements, loc="upper right")

    # Return the cluster labels and the Axes object
    return kmeans.labels_, ax