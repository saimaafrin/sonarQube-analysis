
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Initialize the scaler
    scaler = StandardScaler()
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(df)
    
    # Initialize the KMeans model
    kmeans = KMeans(n_clusters=3, random_state=42)
    
    # Fit the model to the scaled data
    kmeans.fit(scaled_data)
    
    # Get the labels
    labels = kmeans.labels_
    
    return labels