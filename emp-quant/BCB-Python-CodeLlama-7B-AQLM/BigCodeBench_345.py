import pandas as pd
import seaborn as sns
def task_func(df, col1, col2):
    """
    Draw a scatter plot with a regression line for two columns from a DataFrame.

    Parameters:
    df (DataFrame): Input DataFrame.
    col1 (str): Name of the first column.
    col2 (str): Name of the second column.

    Returns:
    Axes: A seaborn axes object.

    Requirements:
    - pandas
    - seaborn

    Raises:
    - Raise ValueError if the input df is not a DataFrame, empty, or does not contain the specified columns.
    - Raise TypeError if df use non-numeric data

    Example:
    >>> import matplotlib.pyplot as plt
    >>> df = pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [2, 4, 6, 8, 10]})
    >>> plot = task_func(df, 'X', 'Y')
    >>> len(plot.collections[0].get_offsets().data)
    5
    >>> plt.close()
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError('df must be a DataFrame')
    if df.empty:
        raise ValueError('df must not be empty')
    if col1 not in df.columns:
        raise ValueError('df must contain column {}'.format(col1))
    if col2 not in df.columns:
        raise ValueError('df must contain column {}'.format(col2))
    if not all(df[col1].dtype == 'int64' or df[col1].dtype == 'float64'):
        raise TypeError('df must contain numeric data in column {}'.format(col1))
    if not all(df[col2].dtype == 'int64' or df[col2].dtype == 'float64'):
        raise TypeError('df must contain numeric data in column {}'.format(col2))

    sns.set(style='whitegrid')
    fig, ax = plt.subplots()
    sns.regplot(x=col1, y=col2, data=df, ax=ax)
    return ax