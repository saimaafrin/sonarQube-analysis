import pandas as pd
from sklearn.cluster import DBSCAN
def task_func(data, cols):
    """
    Perform DBSCAN clustering on the data by transforming it into a DataFrame and recording the clusters in a new column named 'Cluster'.
    
    Parameters:
    - data: A list of lists, where each inner list represents a data point.
    - cols: A list of strings representing the column names for the DataFrame.
    
    Returns:
    - df (DataFrame): The DataFrame with a new 'Cluster' column.
    """
    # Convert the data into a DataFrame
    df = pd.DataFrame(data, columns=cols)
    
    # Perform DBSCAN clustering
    dbscan = DBSCAN(eps=3, min_samples=2)
    df['Cluster'] = dbscan.fit_predict(df)
    
    return df
data = [[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]]
cols = ['x', 'y']