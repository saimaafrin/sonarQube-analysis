
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, items=None, locations=None):
    """
    Generates a bar chart representing the distribution of specified items across given locations.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame with 'Item' and 'Location' columns.
    items : list, optional
        List of items to include in the chart. If not provided, defaults to a predefined list.
    locations : list, optional
        List of locations to include in the chart. If not provided, defaults to a predefined list.

    Returns
    -------
    matplotlib.axes.Axes
        Axes object with the plotted bar chart.

    Raises
    ------
    ValueError
        If 'df' is not a DataFrame, or if 'Item' or 'Location' columns are missing.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a pandas.DataFrame")
    if 'Item' not in df.columns:
        raise ValueError("'Item' column not found in 'df'")
    if 'Location' not in df.columns:
        raise ValueError("'Location' column not found in 'df'")

    # Create a new figure and axis object
    fig, ax = plt.subplots()

    # Set the title and labels
    ax.set_title("Item Distribution")
    ax.set_xlabel("Location")
    ax.set_ylabel("Count")

    # Create a bar chart with the specified items and locations
    if items is not None and locations is not None:
        ax.bar(locations, df[df['Item'].isin(items)]['Location'].value_counts())
    else:
        ax.bar(df['Location'].unique(), df['Item'].value_counts())

    # Set the x-axis tick labels
    ax.set_xticks(df['Location'].unique())
    ax.set_xticklabels(df['Location'].unique())

    # Set the y-axis tick labels
    ax.set_yticks(range(0, max(df['Item'].value_counts()) + 1))
    ax.set_yticklabels(range(0, max(df['Item'].value_counts()) + 1))

    # Return the axis object
    return ax