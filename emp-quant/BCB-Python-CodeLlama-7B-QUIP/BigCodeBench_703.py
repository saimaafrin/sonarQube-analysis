
import pandas as pd
from sklearn.cluster import DBSCAN

def task_func(data, cols):
    # Load the data into a DataFrame
    df = pd.DataFrame(data)

    # Perform DBSCAN clustering with parameters eps=3 and min_samples=2
    clusters = DBSCAN(eps=3, min_samples=2).fit_predict(df)

    # Add a new column to the DataFrame with the cluster labels
    df['Cluster'] = clusters

    return df