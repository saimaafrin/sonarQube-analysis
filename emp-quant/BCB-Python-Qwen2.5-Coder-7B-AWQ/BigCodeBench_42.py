import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
def task_func(data_matrix, n_components=2):
    """
    Apply PCA with n_components components to a 2D data matrix, calculate the mean value of each component,
    and then return the cumulative explained variance of the components in a plot.
    
    Parameters:
    - data_matrix: A 2D numpy array or pandas DataFrame containing the data.
    - n_components: The number of principal components to keep.
    
    Returns:
    - A tuple containing:
        - A pandas DataFrame with the PCA transformed data and the mean of each component.
        - A matplotlib axes object with the plot of the cumulative explained variance.
    """
    # Ensure data_matrix is a numpy array
    if isinstance(data_matrix, pd.DataFrame):
        data_matrix = data_matrix.values
    
    # Apply PCA
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data_matrix)
    
    # Calculate the mean of each component
    mean_values = np.mean(transformed_data, axis=0)
    
    # Create a DataFrame for the transformed data and mean values
    df = pd.DataFrame(transformed_data, columns=[f'Component {i+1}' for i in range(n_components)])
    df['Mean'] = mean_values
    
    # Calculate the cumulative explained variance
    cumulative_explained_variance = np.cumsum(pca.explained_variance_ratio_)
    
    # Plot the cumulative explained variance
    fig, ax = plt.subplots()
    ax.plot(range(1, n_components + 1), cumulative_explained_variance, marker='o')
    ax.set_xlabel('Number of Components')
    ax.set_ylabel('Cumulative Explained Variance')
    
    return df, ax