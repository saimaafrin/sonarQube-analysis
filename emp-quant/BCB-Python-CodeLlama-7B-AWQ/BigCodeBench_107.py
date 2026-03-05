import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def task_func(df, n_clusters=3, random_state=0):
    """
    Performs KMeans clustering on the 'date' and 'value' columns of a DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame to be clustered.
    n_clusters (int, optional): The number of clusters to form. Defaults to 3.
    random_state (int, optional): The random state to use for the clustering. Defaults to 0.

    Returns:
    matplotlib.axes.Axes: The Axes object containing the scatter plot of the clusters.

    Raises:
    ValueError: If the DataFrame is empty or lacks required columns.
    """
    # Check if the DataFrame is empty or lacks required columns
    if df.empty or not set(['date', 'value']).issubset(df.columns):
        raise ValueError('The DataFrame is empty or lacks required columns.')

    # Convert the 'date' column to ordinal
    df['date'] = pd.to_datetime(df['date']).dt.to_period('D')

    # Perform KMeans clustering on the 'date' and 'value' columns
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(df[['date', 'value']])

    # Plot the clusters
    fig, ax = plt.subplots()
    ax.scatter(df['date'], df['value'], c=kmeans.labels_)
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.set_title('KMeans Clustering of Value vs Date')
    return ax
df = pd.DataFrame({'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
                   'value': [1, 2, 3, 4, 5]})