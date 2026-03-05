
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(data_matrix, n_components=2):
    # Apply PCA
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(data_matrix)
    
    # Calculate the mean of each component
    mean_values = pca_result.mean(axis=0)
    
    # Create a DataFrame with the PCA transformed data and the mean of each component
    df = pd.DataFrame(pca_result, columns=[f'Component {i+1}' for i in range(n_components)])
    df['Mean'] = mean_values
    
    # Calculate the cumulative explained variance
    cumulative_explained_variance = pca.explained_variance_ratio_.cumsum()
    
    # Create a plot of the cumulative explained variance
    fig, ax = plt.subplots()
    ax.plot(range(1, n_components + 1), cumulative_explained_variance, marker='o')
    ax.set_xlabel('Number of Components')
    ax.set_ylabel('Cumulative Explained Variance')
    
    return df, ax