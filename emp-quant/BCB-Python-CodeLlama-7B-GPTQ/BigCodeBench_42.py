import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
def task_func(data_matrix, n_components=2):
    # Perform PCA on the data matrix
    pca = PCA(n_components=n_components)
    pca_data = pca.fit_transform(data_matrix)

    # Calculate the mean value of each component
    component_means = pca.components_.mean(axis=0)

    # Create a DataFrame with the PCA transformed data and the mean of each component
    pca_data_df = pd.DataFrame(pca_data, columns=['Component 1', 'Component 2', ...])
    pca_data_df['Mean'] = component_means

    # Create a plot of the cumulative explained variance of the components
    plt.xlabel('Number of Components')
    plt.ylabel('Cumulative Explained Variance')
    plt.plot(range(1, n_components + 1), pca.explained_variance_ratio_)

    return pca_data_df, plt.gca()
data_matrix = pd.DataFrame({'Feature 1': [1, 2, 3, 4, 5], 'Feature 2': [6, 7, 8, 9, 10]})
n_components = 2