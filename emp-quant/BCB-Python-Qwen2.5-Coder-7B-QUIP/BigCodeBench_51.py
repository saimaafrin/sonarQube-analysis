
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def task_func(df, age: int, height: int):
    # Filter the DataFrame based on the specified conditions
    filtered_df = df[(df['Age'] > age) & (df['Height'] > height)]
    
    # Check if the filtered DataFrame has less than 3 columns
    if filtered_df.shape[1] < 3:
        filtered_df['Cluster'] = 0
    else:
        # Perform KMeans clustering
        kmeans = KMeans(n_clusters=3, random_state=0).fit(filtered_df[['Age', 'Height']])
        filtered_df['Cluster'] = kmeans.labels_
    
    # Plot the scatter plot
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(filtered_df['Age'], filtered_df['Height'], c=filtered_df['Cluster'], cmap='viridis')
    plt.xlabel('Age')
    plt.ylabel('Height')
    plt.title('KMeans Clustering based on Age and Height')
    plt.colorbar(scatter)
    
    # Return the DataFrame and the Axes object
    return filtered_df, plt.gca()