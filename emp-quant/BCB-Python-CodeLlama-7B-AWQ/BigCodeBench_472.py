import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
def task_func(myList, n_clusters):
    """
    Cluster a list of 2D points using KMeans and visualize the clusters.
    Note that: This function raises ValueError if it encounters invalid inputs.
    KMeans is performed with random_state = 42 and n_init = 10.
    Scatterplot uses red 'x' markers for cluster centers.
    The function should output with:
        matplotlib.axes._axes.Axes: Axes object with the plotted clusters.
    """
    # Check if the input is valid
    if not isinstance(myList, list):
        raise ValueError("The input must be a list of 2D points.")
    if not all(isinstance(point, tuple) and len(point) == 2 for point in myList):
        raise ValueError("The input list must contain only 2D points.")
    if not isinstance(n_clusters, int):
        raise ValueError("The number of clusters must be an integer.")
    if n_clusters < 1:
        raise ValueError("The number of clusters must be positive.")

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(myList)

    # Visualize the clusters
    fig, ax = plt.subplots()
    ax.scatter(myList[:, 0], myList[:, 1], c=kmeans.labels_)
    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x')
    ax.set_title("Clusters of 2D points")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    return ax
myList = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
n_clusters = 3