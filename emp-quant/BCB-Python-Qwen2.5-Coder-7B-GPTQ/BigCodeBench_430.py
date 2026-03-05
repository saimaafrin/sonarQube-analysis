from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def task_func(df1, df2, column1="feature1", column2="feature2"):
    # Merge the datasets on a common id column (assuming 'id' is the common column)
    merged_df = pd.merge(df1, df2, on='id')
    
    # Extract the features for clustering
    X = merged_df[[column1, column2]]
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=2, n_init=10, random_state=42)
    labels = kmeans.fit_predict(X)
    
    # Plot the results
    fig, ax = plt.subplots()
    scatter = ax.scatter(X[column1], X[column2], c=labels, cmap='viridis')
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.set_title('KMeans Clustering')
    plt.colorbar(scatter)
    
    return labels, ax