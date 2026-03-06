
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty")

    # Perform PCA on the dataframe
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(df)

    # Create a dataframe with the principal components
    principal_components_df = pd.DataFrame(principal_components, columns=['Principal Component 1', 'Principal Component 2'])

    # Create a scatter plot of the two principal components
    fig, ax = plt.subplots()
    ax.scatter(principal_components_df['Principal Component 1'], principal_components_df['Principal Component 2'])
    ax.set_title('2 Component PCA')
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    plt.show()

    return principal_components_df, ax