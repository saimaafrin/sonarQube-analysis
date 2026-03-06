
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(data, n_components=2):
    # Perform PCA on the data
    pca = PCA(n_components=n_components)
    pca_data = pca.fit_transform(data)

    # Create a DataFrame with the transformed data
    df = pd.DataFrame(pca_data, columns=['PC1', 'PC2'])

    # Create a scatter plot of the transformed data
    fig, ax = plt.subplots()
    ax.scatter(df['PC1'], df['PC2'])
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('Scatter Plot of Transformed Data')

    return df, ax