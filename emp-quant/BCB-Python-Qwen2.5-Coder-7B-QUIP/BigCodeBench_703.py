
import pandas as pd
from sklearn.cluster import DBSCAN

def task_func(data, cols):
    # Ensure the input data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame")
    
    # Extract the specified columns from the DataFrame
    selected_data = data[cols]
    
    # Initialize the DBSCAN model with the specified parameters
    dbscan = DBSCAN(eps=3, min_samples=2)
    
    # Fit the model to the data and predict the clusters
    clusters = dbscan.fit_predict(selected_data)
    
    # Add the clusters as a new column to the original DataFrame
    data['Cluster'] = clusters
    
    # Return the DataFrame with the new 'Cluster' column
    return data