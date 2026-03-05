import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def task_func(df, n_clusters=3, random_state=0):
    """
    Convert the 'date' column of a DataFrame to ordinal, perform KMeans clustering on 'date' and 'value' columns, and plot the clusters.
    Required names: x: 'Date (ordinal)' ylabel: 'Value' title: 'KMeans Clustering of Value vs Date'
    The function should raise the exception for: ValueError: If the DataFrame is empty or lacks required columns.
    The function should output with:
        matplotlib.axes.Axes: The Axes object containing the scatter plot of the clusters.
    """
    # Check if the DataFrame is empty or lacks required columns
    if df.empty or 'date' not in df.columns or 'value' not in df.columns:
        raise ValueError("The DataFrame is empty or lacks required columns.")

    # Convert the 'date' column to ordinal
    df['date'] = pd.to_datetime(df['date']).dt.to_period('D')

    # Perform KMeans clustering on 'date' and 'value' columns
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(df[['date', 'value']])

    # Plot the clusters
    fig, ax = plt.subplots()
    ax.scatter(x=df['date'], y=df['value'], c=kmeans.labels_, cmap='viridis')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.set_title('KMeans Clustering of Value vs Date')
    return ax
df = pd.DataFrame({'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
                   'value': [10, 20, 30, 40, 50]})