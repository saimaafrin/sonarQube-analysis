
from itertools import chain
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(L):
    # Convert list of lists to list of integers
    data = [int(x) for sublist in L for x in sublist]

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(data)

    # Get cluster labels
    labels = kmeans.labels_

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(data, labels, c=labels)
    ax.set_xlabel('Data')
    ax.set_ylabel('Cluster')
    ax.set_title('KMeans Clustering')

    return ax