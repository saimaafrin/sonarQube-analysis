import numpy as np
import matplotlib.pyplot as plt
COLORS = ['r', 'g', 'b']
def task_func(df, group_col, value_col, group_name):
    """
    Create a bar subplot of a specific group from the input dataframe.

    Args:
        df (pandas.DataFrame): Input dataframe.
        group_col (str): Name of the column used for grouping.
        value_col (str): Name of the column used for the values.
        group_name (str): Name of the group to be plotted.

    Returns:
        Axes: A matplotlib axes object with the bar chart.

    Raises:
        ValueError: If the group_name does not exist in df.
    """
    # Check if the group_name exists in the dataframe
    if group_name not in df[group_col].unique():
        raise ValueError(f"Group {group_name} does not exist in the dataframe.")

    # Create a bar plot of the specific group
    ax = df.groupby(group_col)[value_col].plot(kind='bar', color=COLORS[0])

    # Set the title, x-axis label, and y-axis label
    ax.set_title(f"Bar chart of {value_col} for {group_name}")
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)

    return ax
df = pd.DataFrame({
    'group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'value': [1, 2, 3, 4, 5, 6]
})