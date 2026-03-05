from itertools import chain
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def task_func(L):
    # Convert list of lists to numpy array
    X = np.array(list(chain.from_iterable(L)))

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(X)

    # Get cluster labels
    labels = kmeans.labels_

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(X[:, 0], X[:, 1], c=labels)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_title('KMeans Clustering')

    return ax
L = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]