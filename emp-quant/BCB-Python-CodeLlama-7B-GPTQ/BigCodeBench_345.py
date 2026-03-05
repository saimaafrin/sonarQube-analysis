import pandas as pd
import seaborn as sns
def task_func(df, col1, col2):
    """
    Draw a scatter plot with a regression line for two columns from a DataFrame.

    Args:
        df (pandas.DataFrame): The input DataFrame.
        col1 (str): The name of the first column.
        col2 (str): The name of the second column.

    Returns:
        Axes: A seaborn axes object.

    Raises:
        ValueError: If the input df is not a DataFrame, empty, or does not contain the specified columns.
        TypeError: If df use non-numeric data.
    """
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")

    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("Input DataFrame is empty")

    # Check if the specified columns exist in the DataFrame
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError("Columns do not exist in the DataFrame")

    # Check if the data in the columns is numeric
    if not df[col1].dtype.kind in "ifnu":
        raise TypeError("Data in column {} is not numeric".format(col1))
    if not df[col2].dtype.kind in "ifnu":
        raise TypeError("Data in column {} is not numeric".format(col2))

    # Draw the scatter plot
    ax = sns.regplot(x=col1, y=col2, data=df)

    return ax
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [2, 4, 6, 8, 10]})