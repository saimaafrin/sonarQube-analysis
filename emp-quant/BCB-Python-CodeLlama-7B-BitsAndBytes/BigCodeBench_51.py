
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(df, age, height):
    # Filter the dataframe based on the specified age and height conditions
    filtered_df = df[(df['Age'] >= age) & (df['Height'] >= height)]

    # If the filtered dataframe has less than 3 columns, add a column 'Cluster' with 0 for each row
    if len(filtered_df.columns) < 3:
        filtered_df['Cluster'] = 0
    else:
        # Perform KMeans clustering on the filtered dataframe
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(filtered_df[['Age', 'Height']])

        # Add a column 'Cluster' to the dataframe with the cluster index of each row
        filtered_df['Cluster'] = kmeans.labels_

    # Plot the data
    fig, ax = plt.subplots()
    ax.scatter(filtered_df['Age'], filtered_df['Height'], c=filtered_df['Cluster'])
    ax.set_xlabel('Age')
    ax.set_ylabel('Height')
    ax.set_title('KMeans Clustering based on Age and Height')

    return filtered_df, ax