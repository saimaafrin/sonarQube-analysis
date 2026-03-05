import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
def task_func(df):
    # Standardize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    # Run KMeans clustering
    kmeans = KMeans(n_clusters=3)
    labels = kmeans.fit_predict(scaled_data)

    return labels
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})