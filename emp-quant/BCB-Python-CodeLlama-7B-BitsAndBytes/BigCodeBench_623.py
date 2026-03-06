
from itertools import chain
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(L):
    # Convert the list of lists into a numpy array
    X = np.array(list(chain.from_iterable(L)))

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(X)

    # Get the cluster labels for each data point
    labels = kmeans.labels_

    # Create a scatter plot with data points color-coded by their cluster
    fig, ax = plt.subplots()
    ax.scatter(X[:, 0], X[:, 1], c=labels)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_title('KMeans Clustering')

    return ax