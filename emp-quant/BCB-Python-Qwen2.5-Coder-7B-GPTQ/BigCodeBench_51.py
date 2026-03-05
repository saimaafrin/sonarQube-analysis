from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
def task_func(df, age: int, height: int):
    # Filter the DataFrame based on the specified conditions
    filtered_df = df[(df['Age'] >= age) & (df['Height'] >= height)]
    
    # Check if the filtered DataFrame has less than 3 columns
    if filtered_df.shape[1] < 3:
        filtered_df['Cluster'] = 0
        return filtered_df, None
    
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=0).fit(filtered_df[['Age', 'Height']])
    filtered_df['Cluster'] = kmeans.labels_
    
    # Plot the scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(filtered_df['Age'], filtered_df['Height'], c=filtered_df['Cluster'], cmap='viridis')
    ax.set_xlabel('Age')
    ax.set_ylabel('Height')
    ax.set_title('KMeans Clustering based on Age and Height')
    plt.colorbar(scatter)
    plt.show()
    
    return filtered_df, ax