from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def task_func(df, age, height):
    # Filter the input DataFrame based on specified 'Age' and 'Height' conditions
    filtered_df = df[(df['Age'] >= age) & (df['Height'] >= height)]

    # If the filtered dataframe has less than 3 columns, add a column 'Cluster' with 0 for each row
    if len(filtered_df.columns) < 3:
        filtered_df['Cluster'] = 0
    else:
        # Do a KMeans clustering (by Age and Height) with 3 clusters and add a column 'Cluster' to the dataframe
        # which corresponds to the cluster index of the cluster to which each row belongs to
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(filtered_df[['Age', 'Height']])
        filtered_df['Cluster'] = kmeans.labels_

    # Plot a scatter plot of the 'Age' and 'height' and colored by the cluster indices
    fig, ax = plt.subplots()
    ax.scatter(filtered_df['Age'], filtered_df['Height'], c=filtered_df['Cluster'])
    ax.set_xlabel('Age')
    ax.set_ylabel('Height')
    ax.set_title('KMeans Clustering based on Age and Height')

    return filtered_df, ax
df = pd.DataFrame({'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],
                   'Height': [170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220]})