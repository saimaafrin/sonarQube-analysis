import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
def task_func(myList, n_clusters):
    """
    Cluster a list of 2D points using KMeans and visualize the clusters.

    Note: This function raises ValueError if it encounters invalid inputs.
    KMeans is performed with random_state = 42 and n_init = 10. Scatterplot
    uses red 'x' markers for cluster centers.

    Parameters:
    - myList (list): List of 2D points.
    - n_clusters (int): Number of clusters to form.

    Returns:
    - matplotlib.axes._axes.Axes: Axes object with the plotted clusters.

    Requirements:
    - matplotlib.pyplot
    - sklearn.cluster.KMeans

    Example:
    >>> myList = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    >>> ax = task_func(myList, 2)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_xticklabels()
    [Text(0.0, 0, '0'), Text(1.0, 0, '1'), Text(2.0, 0, '2'), Text(3.0, 0, '3'), Text(4.0, 0, '4'), Text(5.0, 0, '5'), Text(6.0, 0, '6'), Text(7.0, 0, '7'), Text(8.0, 0, '8'), Text(9.0, 0, '9'), Text(10.0, 0, '10')]
    """
    # Check if myList is a list
    if not isinstance(myList, list):
        raise ValueError("myList must be a list.")

    # Check if myList is a list of lists
    if not all(isinstance(x, list) for x in myList):
        raise ValueError("myList must be a list of lists.")

    # Check if myList is a list of lists of length 2
    if not all(len(x) == 2 for x in myList):
        raise ValueError("myList must be a list of lists of length 2.")

    # Check if n_clusters is an integer
    if not isinstance(n_clusters, int):
        raise ValueError("n_clusters must be an integer.")

    # Check if n_clusters is a positive integer
    if n_clusters <= 0:
        raise ValueError("n_clusters must be a positive integer.")

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(myList)

    # Plot the clusters
    fig, ax = plt.subplots()
    ax.scatter(myList[:, 0], myList[:, 1], c=kmeans.labels_, cmap='rainbow')
    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
               marker='x', s=150, linewidths=5, c='black')
    ax.set_title('Clusters of 2D points')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_xticks(range(len(myList)))
    ax.set_xticklabels(range(len(myList)))
    return ax