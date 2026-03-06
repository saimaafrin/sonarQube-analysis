import pandas as pd
import seaborn as sns
def task_func(data):
    """
    Creates and return a heatmap of the cumulative sum of each column in a dictionary.

    Parameters:
    - data (dict): A dictionary where the keys are the column names and the values are the column values.

    Returns:
    - matplotlib.axes._axes.Axes: The Axes object of the Seaborn heatmap.

    Raises:
    - ValueError: If the DataFrame is empty or if no numeric columns are present.

    Requirements:
    - pandas
    - seaborn

    Notes:
    - Only numeric columns are considered for the heatmap. Non-numeric columns are ignored.

    Example:
    >>> data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    >>> ax = task_func(data)
    """
    if not data:
        raise ValueError('The DataFrame is empty.')

    df = pd.DataFrame(data)
    numeric_columns = df.select_dtypes(include=['number']).columns
    if not numeric_columns:
        raise ValueError('No numeric columns present.')

    df = df[numeric_columns]
    df = df.cumsum()

    ax = sns.heatmap(df, cmap='viridis', linewidths=0.5, linecolor='white', cbar=False)
    ax.set_title('Cumulative sum of each column')
    ax.set_xlabel('Column')
    ax.set_ylabel('Value')

    return ax