
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(data_matrix, n_components=2):
    # Perform PCA on the data matrix
    pca = PCA(n_components=n_components)
    pca_data = pca.fit_transform(data_matrix)

    # Calculate the mean value of each component
    component_means = pca_data.mean(axis=0)

    # Calculate the cumulative explained variance of the components
    cumulative_explained_variance = pca.explained_variance_ / pca.n_components

    # Create a dataframe with the PCA transformed data and the mean of each component
    df = pd.DataFrame(pca_data, columns=['Component 1', 'Component 2', ...])
    df['Mean'] = component_means

    # Plot the cumulative explained variance
    fig, ax = plt.subplots()
    ax.plot(cumulative_explained_variance)
    ax.set_xlabel('Number of Components')
    ax.set_ylabel('Cumulative Explained Variance')
    return df, ax