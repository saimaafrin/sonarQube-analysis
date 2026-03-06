
import pandas as pd
from sklearn.cluster import DBSCAN

def task_func(data, cols):
    # Load the data into a Pandas DataFrame
    df = pd.DataFrame(data, columns=cols)

    # Perform DBSCAN clustering on the data
    dbscan = DBSCAN(eps=3, min_samples=2).fit(df)

    # Create a new column in the DataFrame to store the cluster labels
    df['Cluster'] = dbscan.labels_

    return df