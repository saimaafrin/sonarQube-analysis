
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(df1, df2, column1="feature1", column2="feature2"):
    # Merge datasets
    df = pd.concat([df1, df2], ignore_index=True)
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=2, n_init=10)
    kmeans.fit(df[column1])
    labels = kmeans.labels_
    
    # Plot scatterplot
    fig, ax = plt.subplots()
    ax.scatter(df[column1], df[column2], c=labels)
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.set_title("Clustered Scatterplot")
    
    return labels, ax