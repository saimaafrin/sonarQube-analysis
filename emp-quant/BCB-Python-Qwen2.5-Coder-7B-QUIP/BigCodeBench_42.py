
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(data_matrix, n_components=2):
    # Initialize the PCA model with the specified number of components
    pca = PCA(n_components=n_components)
    
    # Fit the PCA model to the data
    pca.fit(data_matrix)
    
    # Transform the data using the fitted PCA model
    transformed_data = pca.transform(data_matrix)
    
    # Calculate the mean of each component
    component_means = np.abs(transformed_data).mean(axis=0)
    
    # Create a DataFrame to store the transformed data and the mean
    df = pd.DataFrame(transformed_data, columns=[f'Component {i+1}' for i in range(n_components)])
    df['Mean'] = component_means
    
    # Calculate the cumulative explained variance
    cumulative_explained_variance = np.cumsum(pca.explained_variance_ratio_)
    
    # Plot the cumulative explained variance
    fig, ax = plt.subplots()
    ax.plot(range(1, n_components + 1), cumulative_explained_variance, marker='o', linestyle='-', color='b')
    ax.set_xlabel('Number of Components')
    ax.set_ylabel('Cumulative Explained Variance')
    
    # Return the DataFrame and the plot
    return df, ax