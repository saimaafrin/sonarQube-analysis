import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def task_func(s1, s2, n_clusters=3):
    """
    Performs K-Means clustering on data points from two pandas Series and visualizes the clusters.

    Parameters
    ----------
    s1 : pandas.Series
        First pandas Series of data points.
    s2 : pandas.Series
        Second pandas Series of data points.
    n_clusters : int, optional
        Number of clusters to form. Default is 3.

    Returns
    -------
    tuple
        A tuple containing the following elements:
        ndarray
            An array of cluster labels indicating the cluster each data point belongs to.
        matplotlib.axes.Axes
            The Axes object of the plot, which shows the data points colored according to their cluster labels.

    Raises
    ------
    ValueError
        If either s1 or s2 is not a pandas Series, raise "s1 and s2 must be pandas Series".
        If s1 and s2 have different lengths, raise "s1 and s2 must have the same length".
    """
    # Check if s1 and s2 are pandas Series
    if not isinstance(s1, pd.Series) or not isinstance(s2, pd.Series):
        raise ValueError("s1 and s2 must be pandas Series")

    # Check if s1 and s2 have the same length
    if len(s1) != len(s2):
        raise ValueError("s1 and s2 must have the same length")

    # Combine data points from s1 and s2
    data = pd.concat([s1, s2], axis=1)

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data)

    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(data.iloc[:, 0], data.iloc[:, 1], c=kmeans.labels_)
    ax.set_title("K-Means Clustering")

    # Add a legend
    legend_elements = [Line2D([0], [0], marker="o", color=kmeans.cluster_centers_[i], label=f"Cluster {i}") for i in range(n_clusters)]
    ax.legend(handles=legend_elements, loc="upper right")

    return kmeans.labels_, ax
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([6, 7, 8, 9, 10])