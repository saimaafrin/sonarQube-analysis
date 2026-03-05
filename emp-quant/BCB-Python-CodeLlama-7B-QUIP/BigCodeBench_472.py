
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def task_func(myList, n_clusters):
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(myList)
    centers = kmeans.centers_

    # Plot the clusters
    fig, ax = plt.subplots()
    ax.scatter(myList[:, 0], myList[:, 1], c=kmeans.labels_, cmap='red', s=20)
    ax.scatter(centers[:, 0], centers[:, 1], c='red', s=50)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('KMeans Clusters')
    return ax