
import pandas as pd
from sklearn.cluster import DBSCAN

def task_func(data, cols):
    # Convert the input data to a DataFrame
    df = pd.DataFrame(data, columns=cols)
    
    # Select the columns to be used for clustering
    X = df[cols]
    
    # Perform DBSCAN clustering
    dbscan = DBSCAN(eps=3, min_samples=2).fit(X)
    
    # Add the cluster labels to the DataFrame
    df['Cluster'] = dbscan.labels_
    
    return df