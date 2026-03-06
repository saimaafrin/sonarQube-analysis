
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def task_func(myList, n_clusters):
    # Check if the input is valid
    if not isinstance(myList, list) or not all(isinstance(point, tuple) and len(point) == 2 for point in myList):
        raise ValueError("Invalid input: myList must be a list of 2D points")
    if not isinstance(n_clusters, int) or n_clusters < 1:
        raise ValueError("Invalid input: n_clusters must be a positive integer")

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(myList)

    # Create a scatter plot with red 'x' markers for cluster centers
    fig, ax = plt.subplots()
    ax.scatter(myList[:, 0], myList[:, 1], c=kmeans.labels_, cmap='viridis')
    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x')
    ax.set_title('KMeans Clustering')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_zlabel('Cluster')
    return ax