
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(s1, s2, n_clusters=3):
    # Check if s1 and s2 are pandas Series
    if not isinstance(s1, pd.Series) or not isinstance(s2, pd.Series):
        raise ValueError("s1 and s2 must be pandas Series")
    
    # Check if s1 and s2 have the same length
    if len(s1) != len(s2):
        raise ValueError("s1 and s2 must have the same length")
    
    # Combine the data points from s1 and s2
    data = pd.concat([s1, s2], axis=0).values.reshape(-1, 1)
    
    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(data)
    
    # Create a scatter plot
    plt.scatter(range(len(data)), data, c=cluster_labels, cmap='viridis')
    plt.title("K-Means Clustering")
    plt.legend(handles=plt.LineCollection([], [], color='none'), labels=[f"Cluster {i}" for i in range(n_clusters)], title="Clusters")
    
    # Return the cluster labels and the Axes object
    return cluster_labels, plt.gca()