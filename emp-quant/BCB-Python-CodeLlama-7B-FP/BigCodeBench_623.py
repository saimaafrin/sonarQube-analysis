from itertools import chain
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def task_func(L):
    # Convert list of lists to a list of integers
    data = [int(x) for sublist in L for x in sublist]

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(data)

    # Create scatter plot with data points color-coded by their cluster
    fig, ax = plt.subplots()
    ax.scatter(data, c=kmeans.labels_)
    ax.set_xlabel('Data')
    ax.set_ylabel('Cluster')
    ax.set_title('KMeans Clustering')
    return ax
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]