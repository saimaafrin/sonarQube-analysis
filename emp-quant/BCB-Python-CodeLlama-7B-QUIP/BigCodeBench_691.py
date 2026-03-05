
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Scaling the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    # Performing KMeans clustering
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(scaled_data)

    # Getting the labels
    labels = kmeans.labels_

    return labels