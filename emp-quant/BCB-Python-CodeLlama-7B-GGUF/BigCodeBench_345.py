
import pandas as pd
import seaborn as sns

def task_func(df, col1, col2):
    """
    Draw a scatter plot with a regression line for two columns from a DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to draw the plot from.
    col1 : str
        The name of the first column to draw the plot for.
    col2 : str
        The name of the second column to draw the plot for.

    Returns
    -------
    Axes
        A seaborn axes object.

    Raises
    ------
    ValueError
        If the input df is not a DataFrame, empty, or does not contain the specified columns.
    TypeError
        If df uses non-numeric data.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df must be a pandas.DataFrame")
    if df.empty:
        raise ValueError("Input df must not be empty")
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError("Input df must contain the specified columns")
    if not df[col1].dtype.kind in ["i", "f"] or not df[col2].dtype.kind in ["i", "f"]:
        raise TypeError("Input df must use numeric data")

    # Draw the scatter plot with a regression line
    sns.regplot(x=col1, y=col2, data=df)

    # Return the seaborn axes object
    return sns.regplot(x=col1, y=col2, data=df).axes