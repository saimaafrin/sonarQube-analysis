
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(df1, df2, column1="feature1", column2="feature2"):
    # Merge the two datasets
    merged_df = pd.concat([df1, df2], ignore_index=True)

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=2, n_init=10)
    kmeans.fit(merged_df[column1])

    # Get the cluster labels
    labels = kmeans.labels_

    # Plot the data
    fig, ax = plt.subplots()
    ax.scatter(merged_df[column1], merged_df[column2], c=labels)
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.set_title("KMeans Clustering")
    ax.set_xlabel("Cluster Labels")
    ax.set_ylabel("Predicted Cluster")
    ax.set_zlabel("Color")
    return labels, ax