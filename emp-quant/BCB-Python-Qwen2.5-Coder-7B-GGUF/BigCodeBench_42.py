
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(data_matrix, n_components=2):
    # Apply PCA
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data_matrix)
    
    # Create a DataFrame for the transformed data
    df = pd.DataFrame(transformed_data, columns=[f'Component {i+1}' for i in range(n_components)])
    
    # Calculate the mean of each component per row
    df['Mean'] = df.mean(axis=1)
    
    # Calculate the cumulative explained variance
    cumulative_variance = pca.explained_variance_ratio_.cumsum()
    
    # Plot the cumulative explained variance
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, n_components + 1), cumulative_variance, marker='o')
    plt.xlabel('Number of Components')
    plt.ylabel('Cumulative Explained Variance')
    plt.title('Cumulative Explained Variance of PCA Components')
    plt.grid(True)
    plt.show()
    
    return df, plt