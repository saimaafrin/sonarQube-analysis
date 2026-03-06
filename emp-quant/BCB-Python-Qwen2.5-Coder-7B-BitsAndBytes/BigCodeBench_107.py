
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(df, n_clusters=3, random_state=0):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Check if the required columns exist
    required_columns = ['date', 'value']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"DataFrame must contain the columns {required_columns}")
    
    # Convert 'date' column to ordinal
    df['date'] = pd.to_datetime(df['date']).map(dt.datetime.toordinal)
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state).fit(df[['date', 'value']])
    df['cluster'] = kmeans.labels_
    
    # Plot the clusters
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['date'], df['value'], c=df['cluster'], cmap='viridis')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.set_title('KMeans Clustering of Value vs Date')
    plt.colorbar(scatter)
    return ax