
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(df, n_clusters=3, random_state=0):
    if df.empty or 'date' not in df.columns or 'value' not in df.columns:
        raise ValueError("DataFrame is empty or lacks required columns.")
    
    # Convert 'date' column to ordinal
    df['date'] = pd.to_datetime(df['date']).map(pd.Timestamp.toordinal)
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state).fit(df[['date', 'value']])
    df['cluster'] = kmeans.labels_
    
    # Plot the clusters
    fig, ax = plt.subplots()
    ax.scatter(df['date'], df['value'], c=df['cluster'], cmap='viridis')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.set_title('KMeans Clustering of Value vs Date')
    return ax