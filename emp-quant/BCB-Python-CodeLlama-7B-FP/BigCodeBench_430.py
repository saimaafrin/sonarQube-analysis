from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def task_func(df1, df2, column1="feature1", column2="feature2"):
    # Merge datasets
    df = pd.concat([df1, df2], axis=0)

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=2, n_init=10)
    kmeans.fit(df[column1])

    # Get cluster labels
    labels = kmeans.labels_

    # Plot scatterplot
    ax = plt.scatter(df[column1], df[column2], c=labels)

    return labels, ax
df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [1, 2, 3], "feature2": [4, 5, 6]})
df2 = pd.DataFrame({"id": [4, 5, 6], "feature1": [7, 8, 9], "feature2": [10, 11, 12]})