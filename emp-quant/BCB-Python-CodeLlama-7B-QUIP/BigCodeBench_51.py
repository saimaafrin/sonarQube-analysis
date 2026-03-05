
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(df, age, height):
    # Filter the dataframe based on the specified conditions
    filtered_df = df[df['Age'] > age]
    filtered_df = filtered_df[filtered_df['Height'] > height]

    # If the filtered dataframe has less than 3 columns, add a column 'Cluster' with 0 for each row
    if filtered_df.shape[1] < 3:
        filtered_df['Cluster'] = 0
    else:
        # Do KMeans clustering with Age and Height
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(filtered_df[['Age', 'Height']])
        cluster_labels = kmeans.labels_
        filtered_df['Cluster'] = cluster_labels

    # Plot the data
    fig, ax = plt.subplots()
    ax.scatter(filtered_df['Age'], filtered_df['Height'], c=filtered_df['Cluster'])
    ax.set_xlabel('Age')
    ax.set_ylabel('Height')
    ax.set_title('KMeans Clustering based on Age and Height')
    return filtered_df, ax