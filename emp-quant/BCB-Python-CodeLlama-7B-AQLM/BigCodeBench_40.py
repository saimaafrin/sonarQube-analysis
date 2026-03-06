import pandas as pd
import seaborn as sns
from scipy.stats import zscore
def task_func(data_matrix):
    """
    Calculate the Z-values of a 2D data matrix, calculate the mean value of each row and then visualize the correlation matrix of the Z-values with a heatmap.

    Parameters:
    data_matrix (numpy.array): The 2D data matrix of shape (m, n) where m is the number of rows and n is the number of columns.

    Returns:
    tuple: A tuple containing:
      - pandas.DataFrame: A DataFrame with columns 'Feature 1', 'Feature 2', ..., 'Feature n' containing the Z-scores (per matrix row).
                      There is also an additional column 'Mean' the mean of z-score per row.
      - matplotlib.axes.Axes: The Axes object of the plotted heatmap.

    Requirements:
    - pandas
    - seaborn
    - scipy.stats.zscore

    Example:
    >>> import numpy as np
    >>> data = np.array([[6, 8, 1, 3, 4], [-1, 0, 3, 5, 1]])
    >>> df, ax = task_func(data)
    >>> print(df)
       Feature 1  Feature 2  Feature 3  Feature 4  Feature 5          Mean
    0   0.662085   1.489691  -1.406930  -0.579324  -0.165521 -2.053913e-16
    1  -1.207020  -0.742781   0.649934   1.578410  -0.278543 -3.330669e-17
    """
    z_values = zscore(data_matrix, axis=1)
    z_values_df = pd.DataFrame(z_values, columns=['Feature ' + str(i) for i in range(1, data_matrix.shape[1] + 1)])
    z_values_df['Mean'] = z_values_df.mean(axis=1)
    ax = sns.heatmap(z_values_df.corr(), annot=True, fmt='.2f', cmap='coolwarm')
    return z_values_df, ax