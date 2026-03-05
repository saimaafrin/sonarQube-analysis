
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(data, n_components=2):
    # Perform PCA on the data
    pca = PCA(n_components=n_components)
    pca_data = pca.fit_transform(data)

    # Create a DataFrame with the transformed data
    pca_data_df = pd.DataFrame(pca_data, columns=['PC1', 'PC2'])

    # Create a scatter plot of the transformed data
    fig, ax = plt.subplots()
    ax.scatter(pca_data_df['PC1'], pca_data_df['PC2'])
    ax.set_xlabel('PC1')
    ax.set_ylabel('PC2')
    ax.set_title('PCA of the data')

    # Return the DataFrame and the Axes object
    return pca_data_df, ax