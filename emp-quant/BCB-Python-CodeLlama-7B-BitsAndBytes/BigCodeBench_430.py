
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