from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def task_func(df1, df2, column1="feature1", column2="feature2"):
    # Merge the datasets on a common id column (assuming 'id' is the common column)
    merged_df = pd.merge(df1, df2, on='id')
    
    # Select the feature columns for clustering
    X = merged_df[[column1, column2]]
    
    # Initialize and fit the KMeans model
    kmeans = KMeans(n_clusters=2, n_init=10, random_state=42)
    labels = kmeans.fit_predict(X)
    
    # Plot the scatterplot
    fig, ax = plt.subplots()
    ax.scatter(X[column1], X[column2], c=labels, cmap='viridis')
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.set_title('KMeans Clustering')
    
    return labels, ax