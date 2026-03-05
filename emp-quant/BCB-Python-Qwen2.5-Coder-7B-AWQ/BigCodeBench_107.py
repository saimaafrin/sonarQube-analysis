import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def task_func(df, n_clusters=3, random_state=0):
    """
    Convert the 'date' column of a DataFrame to ordinal, perform KMeans clustering on 'date' and 'value' columns,
    and plot the clusters.

    Parameters:
    df (pd.DataFrame): Input DataFrame with 'date' and 'value' columns.
    n_clusters (int): Number of clusters for KMeans.
    random_state (int): Random state for reproducibility.

    Returns:
    matplotlib.axes.Axes: The Axes object containing the scatter plot of the clusters.

    Raises:
    ValueError: If the DataFrame is empty or lacks required columns.
    """
    # Check if the DataFrame is empty or lacks required columns
    if df.empty or 'date' not in df.columns or 'value' not in df.columns:
        raise ValueError("DataFrame is empty or lacks required columns.")

    # Convert 'date' column to ordinal
    df['date'] = pd.to_datetime(df['date']).map(pd.Timestamp.toordinal)

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    df['cluster'] = kmeans.fit_predict(df[['date', 'value']])

    # Plot the clusters
    fig, ax = plt.subplots()
    ax.scatter(df['date'], df['value'], c=df['cluster'], cmap='viridis')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.set_title('KMeans Clustering of Value vs Date')

    return ax