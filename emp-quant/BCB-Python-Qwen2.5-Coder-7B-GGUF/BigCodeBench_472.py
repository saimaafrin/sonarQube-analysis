
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def task_func(myList, n_clusters):
    # Check if myList is a list and contains at least one element
    if not isinstance(myList, list) or len(myList) == 0:
        raise ValueError("myList must be a non-empty list")
    
    # Check if each element in myList is a list of exactly two elements
    for point in myList:
        if not isinstance(point, list) or len(point) != 2:
            raise ValueError("Each element in myList must be a list of exactly two elements")
    
    # Check if n_clusters is an integer and greater than 0
    if not isinstance(n_clusters, int) or n_clusters <= 0:
        raise ValueError("n_clusters must be a positive integer")
    
    # Convert myList to a numpy array
    points = np.array(myList)
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10).fit(points)
    
    # Create a scatter plot of the points
    fig, ax = plt.subplots()
    ax.scatter(points[:, 0], points[:, 1], c=kmeans.labels_)
    
    # Plot the cluster centers
    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', color='red')
    
    return ax