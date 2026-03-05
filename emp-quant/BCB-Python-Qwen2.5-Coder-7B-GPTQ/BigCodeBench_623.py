from itertools import chain
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def task_func(L):
    # Flatten the list of lists into a single list of integers
    flat_list = list(chain.from_iterable(L))
    
    # Convert the flat list into a numpy array
    data = np.array(flat_list).reshape(-1, 1)
    
    # Apply KMeans clustering with 2 clusters
    kmeans = KMeans(n_clusters=2).fit(data)
    
    # Get the cluster labels for each data point
    labels = kmeans.labels_
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(range(len(labels)), labels, c=labels, cmap='viridis')
    
    # Return the Axes object
    return ax