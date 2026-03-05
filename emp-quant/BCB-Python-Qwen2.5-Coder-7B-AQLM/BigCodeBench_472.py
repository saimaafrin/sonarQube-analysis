
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def task_func(myList, n_clusters):
    if not isinstance(myList, list) or not all(isinstance(point, list) and len(point) == 2 for point in myList):
        raise ValueError("Input must be a list of 2D points.")
    if not isinstance(n_clusters, int) or n_clusters <= 0:
        raise ValueError("n_clusters must be a positive integer.")
    
    # Convert the list of points to a numpy array
    points = np.array(myList)
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10).fit(points)
    
    # Get the cluster centers and labels
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    
    # Create a scatter plot of the points
    plt.scatter(points[:, 0], points[:, 1], c=labels, cmap='viridis')
    
    # Plot the cluster centers
    plt.scatter(centers[:, 0], centers[:, 1], marker='x', color='red')
    
    # Return the Axes object
    return plt.gca()