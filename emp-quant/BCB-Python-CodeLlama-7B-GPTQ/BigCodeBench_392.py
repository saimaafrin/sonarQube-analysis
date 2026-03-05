import numpy as np
import matplotlib.pyplot as plt
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
        Name of the column used for the value.
    group_name : str
        Name of the group to be plotted.

    Returns
    -------
    Axes
        A matplotlib axes object with the bar chart.

    Raises
    ------
    ValueError
        If the group_name does not exist in df.
    """
    # Check if the group_name exists in df
    if group_name not in df[group_col].unique():
        raise ValueError(f"Group {group_name} does not exist in df.")

    # Create a bar plot
    fig, ax = plt.subplots()
    ax.bar(df[group_col], df[value_col], color=COLORS[0])
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)
    ax.set_title(f"Bar chart of {value_col} for {group_name}")

    return ax
df = pd.DataFrame({
    "group": ["A", "A", "B", "B", "C", "C"],
    "value": [1, 2, 3, 4, 5, 6]
})