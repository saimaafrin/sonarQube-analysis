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
    
    # Initialize and fit the KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(points)
    
    # Get the cluster centers and labels
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    
    # Create a scatter plot of the points
    ax = plt.scatter(points[:, 0], points[:, 1], c=labels, cmap='viridis')
    
    # Plot the cluster centers
    ax.scatter(centers[:, 0], centers[:, 1], marker='x', color='red', s=200, linewidths=3)
    
    # Return the Axes object
    return ax