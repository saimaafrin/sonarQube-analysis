
from itertools import chain
import numpy as np
from sklearn.cluster import KMeans

def task_func(L):
    # Convert the list of lists to a numpy array
    data = np.array(L)

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(data)

    # Get the cluster labels
    labels = kmeans.labels_

    # Create a scatter plot with color-coded clusters
    fig, ax = plt.subplots()
    ax.scatter(data[:, 0], data[:, 1], c=labels)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('KMeans Clustering')
    return ax