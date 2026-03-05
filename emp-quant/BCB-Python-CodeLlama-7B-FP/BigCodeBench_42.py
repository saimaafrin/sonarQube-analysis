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
    df = pd.DataFrame(pca_data, columns=['Component 1', 'Component 2', ...])
    df['Mean'] = mean_values

    # Create a plot of the cumulative explained variance of the components
    plt.plot(range(1, n_components + 1), pca.explained_variance_ratio_)
    plt.xlabel('Number of Components')
    plt.ylabel('Cumulative Explained Variance')
    plt.title('Cumulative Explained Variance of PCA Components')

    return df, plt.gca()
data_matrix = pd.DataFrame({'Feature 1': [1, 2, 3, 4, 5], 'Feature 2': [2, 4, 6, 8, 10]})
n_components = 2