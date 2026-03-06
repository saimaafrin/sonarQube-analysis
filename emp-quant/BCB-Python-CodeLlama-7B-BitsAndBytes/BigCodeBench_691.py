
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Scaling the data using StandardScaler
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    # Running KMeans clustering on scaled data
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(scaled_data)

    # Returning the labels
    return kmeans.labels_