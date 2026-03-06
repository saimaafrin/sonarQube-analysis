
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(df1, df2, column1="feature1", column2="feature2"):
    # Merge the two dataframes on their 'id' columns
    merged_df = pd.merge(df1, df2, on='id')
    
    # Extract the features for clustering
    X = merged_df[[column1, column2]]
    
    # Initialize and fit the KMeans model
    kmeans = KMeans(n_clusters=2, n_init=10)
    labels = kmeans.fit_predict(X)
    
    # Plotting the results
    fig, ax = plt.subplots()
    scatter = ax.scatter(merged_df[column1], merged_df[column2], c=labels, cmap='viridis')
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.set_title('KMeans Clustering')
    plt.colorbar(scatter)
    
    return labels, ax