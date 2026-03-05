
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(data_matrix, n_components=2):
    # Perform PCA with n_components components
    pca = PCA(n_components=n_components)
    pca_data = pca.fit_transform(data_matrix)

    # Calculate the mean value of each component
    mean_values = pca.mean_

    # Create a DataFrame with the PCA transformed data and the mean of each component
    pca_data_df = pd.DataFrame(pca_data, columns=['Component 1', 'Component 2', ...])
    pca_data_df['Mean'] = mean_values

    # Plot the cumulative explained variance of the components
    plt.xlabel('Number of Components')
    plt.ylabel('Cumulative Explained Variance')
    plt.plot(pca_data_df['Mean'])
    plt.show()

    return pca_data_df, plt.gca()