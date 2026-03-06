
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(s1, s2, n_clusters=3):
    # Check if both inputs are pandas Series
    if not isinstance(s1, pd.Series) or not isinstance(s2, pd.Series):
        raise ValueError("s1 and s2 must be pandas Series")
    
    # Check if both Series have the same length
    if len(s1) != len(s2):
        raise ValueError("s1 and s2 must have the same length")
    
    # Combine the Series into a single DataFrame
    data = pd.DataFrame({'s1': s1, 's2': s2})
    
    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters)
    cluster_labels = kmeans.fit_predict(data)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    colors = ['red', 'blue', 'green']  # Assuming up to 3 clusters
    for i, label in enumerate(cluster_labels):
        ax.scatter(i, i, c=colors[label], label=f'Cluster {label}' if i == 0 else "")
    
    # Set plot title and legend
    ax.set_title('K-Means Clustering')
    ax.legend()
    
    return cluster_labels, ax