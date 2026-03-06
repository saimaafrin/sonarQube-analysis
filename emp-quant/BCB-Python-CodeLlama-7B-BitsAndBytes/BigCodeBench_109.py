
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
    if 'Item' not in df.columns or 'Location' not in df.columns:
        raise ValueError("'Item' and 'Location' columns must be present in the DataFrame")

    # Create a new figure and axis object
    fig, ax = plt.subplots()

    # Set the title and labels
    ax.set_title("Item Distribution Across Locations")
    ax.set_xlabel("Location")
    ax.set_ylabel("Item Count")

    # Create a bar chart of the item distribution
    if items is not None:
        df_items = df[df['Item'].isin(items)]
    else:
        df_items = df
    if locations is not None:
        df_locations = df[df['Location'].isin(locations)]
    else:
        df_locations = df
    ax.bar(df_locations['Location'], df_items['Item'].value_counts())

    # Return the axis object
    return ax