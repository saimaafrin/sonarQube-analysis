
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
    
    # Combine the Series into a single DataFrame
    data = pd.DataFrame({'s1': s1, 's2': s2})
    
    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)
    cluster_labels = kmeans.labels_
    
    # Create a scatter plot
    plt.scatter(data['s1'], data['s2'], c=cluster_labels, cmap='viridis')
    plt.title("K-Means Clustering")
    plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='r', markersize=10),
                       plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='g', markersize=10),
                       plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='b', markersize=10)])
    
    # Return the cluster labels and the Axes object
    return cluster_labels, plt.gca()