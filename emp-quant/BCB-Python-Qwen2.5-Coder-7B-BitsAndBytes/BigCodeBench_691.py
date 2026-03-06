
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Standardize the features to have mean=0 and variance=1
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    
    # Run KMeans clustering
    kmeans = KMeans(n_clusters=3)  # Assuming we want to find 3 clusters
    labels = kmeans.fit_predict(df_scaled)
    
    return labels