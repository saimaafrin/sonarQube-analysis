
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def task_func(myList, n_clusters):
    # Check if myList is not empty and contains only lists of length 2
    if not myList or not all(isinstance(point, list) and len(point) == 2 for point in myList):
        raise ValueError("Invalid input: myList must be a non-empty list of 2D points.")
    
    # Convert myList to a numpy array
    points = np.array(myList)
    
    # Initialize KMeans with specified parameters
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    
    # Fit the model to the data
    kmeans.fit(points)
    
    # Get the cluster labels and centroids
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    
    # Create a scatter plot of the points
    fig, ax = plt.subplots()
    ax.scatter(points[:, 0], points[:, 1], c=labels, cmap='viridis')
    
    # Plot the cluster centers
    ax.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red')
    
    return ax