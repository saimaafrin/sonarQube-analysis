
import pandas as pd
from sklearn.cluster import DBSCAN

def task_func(data, cols):
    # Convert the input data to a DataFrame
    df = pd.DataFrame(data, columns=cols)
    
    # Initialize the DBSCAN model with eps=3 and min_samples=2
    dbscan = DBSCAN(eps=3, min_samples=2)
    
    # Fit the model to the data and predict the clusters
    df['Cluster'] = dbscan.fit_predict(df[cols])
    
    return df