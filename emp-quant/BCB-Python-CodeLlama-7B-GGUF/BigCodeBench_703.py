
import pandas as pd
from sklearn.cluster import DBSCAN

def task_func(data, cols):
    # Transform the data into a DataFrame
    df = pd.DataFrame(data, columns=cols)

    # Perform DBSCAN clustering with eps=3 and min_samples=2
    dbscan = DBSCAN(eps=3, min_samples=2)
    dbscan.fit(df)

    # Add a new column to the DataFrame with the cluster labels
    df['Cluster'] = dbscan.labels_

    return df