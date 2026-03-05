
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def task_func(myList, n_clusters):
    # Check if myList is a list of lists and n_clusters is an integer
    if not isinstance(myList, list) or not all(isinstance(point, list) for point in myList) or not isinstance(n_clusters, int):
        raise ValueError("Invalid input. myList should be a list of lists and n_clusters should be an integer.")
    
    # Check if myList is not empty and n_clusters is greater than 0
    if not myList or n_clusters <= 0:
        raise ValueError("Invalid input. myList should not be empty and n_clusters should be greater than 0.")
    
    # Check if n_clusters is less than or equal to the number of points in myList
    if n_clusters > len(myList):
        raise ValueError("Invalid input. n_clusters should be less than or equal to the number of points in myList.")
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(myList)
    labels = kmeans.labels_
    
    # Plot the clusters
    plt.scatter(myList[:, 0], myList[:, 1], c=labels, cmap='viridis')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', color='red', s=200, alpha=0.5)
    plt.show()
    
    # Return the Axes object
    return plt.gca()