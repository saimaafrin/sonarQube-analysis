import pandas as pd
import seaborn as sns
def task_func(df, col1, col2):
    """
    Draw a scatter plot with a regression line for two columns from a DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        col1 (str): The name of the first column to plot.
        col2 (str): The name of the second column to plot.

    Returns:
        Axes: A seaborn axes object.

    Raises:
        ValueError: If the input df is not a DataFrame, empty, or does not contain the specified columns.
        TypeError: If df uses non-numeric data.
    """
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")

    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("Input DataFrame is empty")

    # Check if the specified columns are in the DataFrame
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError("Columns not found in DataFrame")

    # Check if the data is numeric
    if not df[col1].dtype.kind in "ifnu":
        raise TypeError("Data must be numeric")

    # Create a seaborn Axes object
    ax = sns.regplot(x=col1, y=col2, data=df)

    return ax
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [2, 4, 6, 8, 10]})