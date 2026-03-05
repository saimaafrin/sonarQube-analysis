
import numpy as np
import matplotlib.pyplot as plt

# Constants
COLORS = ['r', 'g', 'b']

def task_func(df, group_col, value_col, group_name):
    """
    Create a bar subplot of a specific group from the input dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.
    group_col : str
        Name of the column used for grouping.
    value_col : str
        Name of the column used for the values.
    group_name : str
        Name of the group to plot.

    Returns
    -------
    Axes
        A matplotlib axes object with the bar chart.

    Raises
    ------
    ValueError
        If the group_name does not exist in df.
    """
    if group_name not in df[group_col].unique():
        raise ValueError(f"Group {group_name} does not exist in df.")

    # Create a bar plot
    ax = df.groupby(group_col)[value_col].sum().plot(kind='bar', color=COLORS[0])

    # Set the title, x-axis label, and y-axis label
    ax.set_title(f"Bar chart of {value_col} for {group_name}")
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)

    return ax