import pandas as pd
from sklearn.cluster import DBSCAN
def task_func(data, cols):
    """
    Perform DBSCAN clustering on the data by transforming it into a DataFrame and recording the clusters in a new column named 'Cluster'.
    
    Parameters:
    - data: A 2D array-like structure containing the data points.
    - cols: A list of column names for the DataFrame.
    
    Returns:
    - df (DataFrame): The DataFrame with a new 'Cluster' column.
    """
    # Convert the data into a DataFrame
    df = pd.DataFrame(data, columns=cols)
    
    # Initialize the DBSCAN model with eps=3 and min_samples=2
    dbscan = DBSCAN(eps=3, min_samples=2)
    
    # Fit the model to the data and predict the clusters
    df['Cluster'] = dbscan.fit_predict(df)
    
    return df