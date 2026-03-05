
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

def task_func(df1, df2, column1="feature1", column2="feature2"):
    # Concatenate the datasets
    combined_df = pd.concat([df1, df2], ignore_index=True)
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=2, init='k-means++', n_init=10, random_state=42)
    labels = kmeans.fit_predict(combined_df[[column1, column2]])
    
    # Plot the scatterplot
    fig, ax = plt.subplots()
    ax.scatter(combined_df[column1], combined_df[column2], c=labels, cmap='viridis')
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.set_title('KMeans Clustering')
    
    return labels, ax