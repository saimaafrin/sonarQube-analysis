from itertools import chain
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def task_func(L):
    # Convert list of lists to list of integers
    data = [list(chain.from_iterable(row)) for row in L]
    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(data)
    # Get cluster labels
    labels = kmeans.labels_
    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(data[:, 0], data[:, 1], c=labels)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_title('KMeans Clustering')
    return ax