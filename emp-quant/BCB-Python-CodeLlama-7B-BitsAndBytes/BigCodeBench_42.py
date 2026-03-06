
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(data_matrix, n_components=2):
    # Perform PCA on the data matrix
    pca = PCA(n_components=n_components)
    pca_data = pca.fit_transform(data_matrix)

    # Calculate the mean value of each component
    mean_values = pca.mean_

    # Create a DataFrame with the PCA transformed data and the mean of each component
    df = pd.DataFrame(pca_data, columns=['Component 1', 'Component 2', ...])
    df['Mean'] = mean_values

    # Plot the cumulative explained variance of the components
    plt.plot(range(1, n_components+1), pca.explained_variance_ratio_, label='Cumulative Explained Variance')
    plt.xlabel('Number of Components')
    plt.ylabel('Cumulative Explained Variance')
    plt.title('Cumulative Explained Variance of PCA Components')
    plt.legend()

    return df, plt.gca()

df, ax = task_func(data_matrix, n_components)
print(df)