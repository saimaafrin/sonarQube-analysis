
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty")
    pca = PCA(n_components=2)
    pca.fit(df)
    principal_components = pca.components_
    principal_components_df = pd.DataFrame(
        data=principal_components,
        columns=['Principal Component 1', 'Principal Component 2']
    )
    fig, ax = plt.subplots()
    ax.scatter(principal_components_df['Principal Component 1'], principal_components_df['Principal Component 2'])
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title('2 Component PCA')
    return principal_components_df, fig