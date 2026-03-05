
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Standardize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    # Run KMeans clustering
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(scaled_data)

    # Get the cluster labels
    labels = kmeans.labels_

    return labels