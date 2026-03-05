import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
def task_func(myList, n_clusters):
    """
    Cluster a list of 2D points using KMeans and visualize the clusters.
    
    Parameters:
    myList (list of tuples): A list of 2D points.
    n_clusters (int): The number of clusters to form.
    
    Returns:
    matplotlib.axes._axes.Axes: Axes object with the plotted clusters.
    """
    # Convert the list of tuples to a numpy array
    points = np.array(myList)
    
    # Check if the input list is empty or if n_clusters is not a positive integer
    if len(points) == 0 or not isinstance(n_clusters, int) or n_clusters <= 0:
        raise ValueError("Invalid input: myList must be non-empty and n_clusters must be a positive integer.")
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(points)
    
    # Create a scatter plot of the points
    fig, ax = plt.subplots()
    ax.scatter(points[:, 0], points[:, 1], c=kmeans.labels_)
    
    # Plot the cluster centers
    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x')
    
    return ax