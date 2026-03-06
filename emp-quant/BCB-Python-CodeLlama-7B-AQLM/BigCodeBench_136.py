import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
def task_func(df):
    """
    Perform Principal Component Analysis (PCA) on the dataframe and visualize the two main components.

    Parameters:
        df (DataFrame): The input dataframe containing numerical data.

    Returns:
        DataFrame: A pandas DataFrame with the principal components named 'Principal Component 1' and 'Principal Component 2'.
        Axes: A Matplotlib Axes object representing the scatter plot of the two principal components. The plot includes:
              - Title: '2 Component PCA'
              - X-axis label: 'Principal Component 1'
              - Y-axis label: 'Principal Component 2'

    Raises:
        ValueError: If the input is not a DataFrame, or if the DataFrame is empty.

    Requirements:
        - pandas
        - sklearn.decomposition
        - matplotlib.pyplot

    Example:
        >>> df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        >>> pca_df, ax = task_func(df)
        >>> plt.show()
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError('Input must be a DataFrame.')
    if df.empty:
        raise ValueError('DataFrame is empty.')

    pca = PCA(n_components=2)
    pca_df = pd.DataFrame(pca.fit_transform(df), columns=['Principal Component 1', 'Principal Component 2'])

    ax = pca_df.plot.scatter(x='Principal Component 1', y='Principal Component 2', figsize=(10, 10), title='2 Component PCA',
                             xlabel='Principal Component 1', ylabel='Principal Component 2')

    return pca_df, ax