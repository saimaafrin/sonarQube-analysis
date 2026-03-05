import numpy as np
import matplotlib.pyplot as plt
COLORS = ['r', 'g', 'b']
def task_func(df, group_col, value_col):
    """
    Create a bar chart of data in multiple groups with error bars.
    """
    # Check if the 'Value' column has non-numeric values
    if not all(df[value_col].apply(lambda x: isinstance(x, (int, float)))):
        raise TypeError("The 'Value' column has non-numeric values.")
    # Create a list of unique groups
    groups = df[group_col].unique()
    # Create a list of colors
    colors = COLORS * len(groups)
    # Create a dictionary of data for each group
    data = {group: df[df[group_col] == group][value_col].tolist() for group in groups}
    # Create a dictionary of error bars for each group
    errors = {group: df[df[group_col] == group][value_col].std() for group in groups}
    # Create a figure and axis
    fig, ax = plt.subplots()
    # Create a bar chart
    ax.bar(groups, data, yerr=errors, color=colors)
    # Set the plot title
    ax.set_title(f"Bar chart of {value_col} by {group_col}")
    # Set the xlabel and ylabel
    ax.set_xlabel(value_col)
    ax.set_ylabel(group_col)
    # Return the axis
    return ax
df = pd.DataFrame({"Group": ["A", "A", "B", "B", "C", "C"], "Value": [1, 2, 3, 4, 5, 6]})