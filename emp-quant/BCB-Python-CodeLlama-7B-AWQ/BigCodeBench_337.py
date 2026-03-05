import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
COLORS = ['r', 'g', 'b']
def task_func(df, group_col, value_col):
    """
    Create a bar chart of data in multiple groups with error bars.
    """
    # Check if the 'Value' has non-numeric values
    if not all(df[value_col].apply(lambda x: isinstance(x, (int, float)))):
        raise TypeError("The 'Value' has non-numeric values.")

    # Create a list of unique groups
    groups = df[group_col].unique()

    # Create a list of colors
    colors = COLORS * len(groups)
    colors = colors[:len(groups)]

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Create a bar chart
    for i, group in enumerate(groups):
        # Get the data for the current group
        group_data = df[df[group_col] == group]

        # Get the mean and standard deviation for the current group
        mean = group_data[value_col].mean()
        std = group_data[value_col].std()

        # Create a bar
        ax.bar(i, mean, yerr=std, color=colors[i])

    # Set the title, xlabel, and ylabel
    ax.set_title(f"Bar chart of {value_col} by {group_col}")
    ax.set_xlabel(value_col)
    ax.set_ylabel(group_col)

    # Return the axis
    return ax
df = pd.DataFrame({
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [1, 2, 3, 4, 5, 6]
})