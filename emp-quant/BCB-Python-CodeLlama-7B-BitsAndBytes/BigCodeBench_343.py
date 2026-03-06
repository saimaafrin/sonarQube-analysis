
import pandas as pd
import matplotlib.pyplot as plt

# Constants for pie chart colors
COLORS = ['r', 'g', 'b', 'y', 'm']

def task_func(df, col, title=None):
    """
    Draw a pie chart of the number of unique values in a given DataFrame column.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the column to plot.
    col : str
        The name of the column to plot.
    title : str, optional
        The title of the pie chart.

    Returns
    -------
    axes : matplotlib.axes.Axes
        The axes object representing the pie chart.

    Raises
    ------
    ValueError
        If the input df is not a DataFrame, or if the column is not present in the DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df must be a DataFrame.")
    if col not in df.columns:
        raise ValueError("Column '{}' not found in DataFrame.".format(col))

    # Get the unique values in the column
    unique_vals = df[col].unique()

    # Create a pie chart with the unique values as slices
    fig, ax = plt.subplots()
    ax.pie(unique_vals, colors=COLORS, autopct='%1.1f%%')

    # Set the title of the pie chart
    if title is not None:
        ax.set_title(title)

    return ax