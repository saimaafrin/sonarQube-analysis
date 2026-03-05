import pandas as pd
from sklearn.cluster import DBSCAN
def task_func(data, cols):
    # Transform the data into a DataFrame
    df = pd.DataFrame(data, columns=cols)

    # Perform DBSCAN clustering
    dbscan = DBSCAN(eps=3, min_samples=2)
    clusters = dbscan.fit_predict(df)

    # Add the clusters to the DataFrame
    df['Cluster'] = clusters

    return df
data = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
cols = ['A', 'B']