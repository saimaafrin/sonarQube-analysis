import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
TARGET_VALUES = np.array([1, 3, 4])
def task_func(df):
    """
    Replace all elements in DataFrame columns that do not exist in the TARGET_VALUES array with zeros, then perform a Box-Cox transformation on each column (if data is not constant, add 1 to account for zeros) and display the resulting KDE plots.

    Parameters:
        - df (pandas.DataFrame): The input pandas DataFrame with positive values.

    Returns:
        - pandas.DataFrame: The transformed DataFrame after Box-Cox transformation.
        - matplotlib.figure.Figure: Figure containing KDE plots of the transformed columns.

    Requirements:
    - numpy
    - scipy.stats
    - matplotlib.pyplot

    Example:
    >>> np.random.seed(42)
    >>> df = pd.DataFrame(np.random.randint(1, 10, size=(100, 5)), columns=list('ABCDE'))  # Values should be positive for Box-Cox
    >>> transformed_df, fig = task_func(df)
    >>> print(transformed_df.head(2))
              A         B    C    D         E
    0  0.000000  0.566735  0.0  0.0  0.000000
    1  0.530493  0.000000  0.0  0.0  0.607007
    """
    # Replace all elements in DataFrame columns that do not exist in the TARGET_VALUES array with zeros
    df = df.replace(to_replace=np.setdiff1d(df.columns, TARGET_VALUES), value=0)

    # Perform a Box-Cox transformation on each column (if data is not constant, add 1 to account for zeros)
    transformed_df = df.apply(lambda x: stats.boxcox(x + 1) if x.std() > 0 else x)

    # Display the resulting KDE plots
    fig = plt.figure(figsize=(12, 6))
    for i, col in enumerate(transformed_df.columns):
        plt.subplot(1, 3, i + 1)
        plt.title(col)
        plt.hist(transformed_df[col], bins=100, density=True)
        plt.xlabel(col)
        plt.ylabel('Density')

    return transformed_df, fig