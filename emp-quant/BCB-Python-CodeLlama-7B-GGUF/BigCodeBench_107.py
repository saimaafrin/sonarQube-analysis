
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(df, n_clusters=3, random_state=0):
    if df.empty or 'date' not in df.columns or 'value' not in df.columns:
        raise ValueError("DataFrame is empty or lacks required columns")

    # Convert 'date' column to ordinal
    df['date'] = pd.to_datetime(df['date']).dt.to_period('D')

    # Perform KMeans clustering on 'date' and 'value' columns
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(df[['date', 'value']])

    # Plot the clusters
    fig, ax = plt.subplots()
    ax.scatter(df['date'], df['value'], c=kmeans.labels_)
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.set_title('KMeans Clustering of Value vs Date')
    return ax