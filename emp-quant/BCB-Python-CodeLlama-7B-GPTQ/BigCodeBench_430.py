from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def task_func(df1, df2, column1="feature1", column2="feature2"):
    # Merge datasets
    df = pd.concat([df1, df2], axis=0, ignore_index=True)

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=2, n_init=10)
    kmeans.fit(df[column1])
    labels = kmeans.labels_

    # Plot scatterplot
    fig, ax = plt.subplots()
    ax.scatter(df[column1], df[column2], c=labels)
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.set_title("Cluster labels")

    return labels, ax
df1 = pd.DataFrame({"id": [1, 2, 3, 4, 5], "feature1": [1, 2, 3, 4, 5], "feature2": [1, 2, 3, 4, 5]})
df2 = pd.DataFrame({"id": [6, 7, 8, 9, 10], "feature1": [6, 7, 8, 9, 10], "feature2": [6, 7, 8, 9, 10]})