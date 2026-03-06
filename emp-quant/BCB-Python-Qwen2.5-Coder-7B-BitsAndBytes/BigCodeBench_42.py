
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(data_matrix, n_components=2):
    # Apply PCA with n_components components
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data_matrix)
    
    # Calculate the mean value of each component for each row
    means = np.mean(transformed_data, axis=0)
    
    # Create a DataFrame with the transformed data and the mean values
    df = pd.DataFrame(transformed_data, columns=[f'Component {i+1}' for i in range(n_components)])
    df['Mean'] = means
    
    # Calculate the cumulative explained variance
    cum_explained_variance = np.cumsum(pca.explained_variance_ratio_)
    
    # Plot the cumulative explained variance
    fig, ax = plt.subplots()
    ax.plot(range(1, n_components + 1), cum_explained_variance, marker='o')
    ax.set_xlabel('Number of Components')
    ax.set_ylabel('Cumulative Explained Variance')
    
    return df, ax

    # Call the function
    result_df, plot_ax = task_func(data_matrix, n_components=2)
    
    # Print the resulting DataFrame
    print(result_df)
    
    # Show the plot
    plot_ax.figure.show()