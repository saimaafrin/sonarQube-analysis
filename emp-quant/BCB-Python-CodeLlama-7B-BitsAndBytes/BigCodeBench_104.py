
import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle

def task_func(df, groups=['A', 'B', 'C', 'D', 'E']):
    # Check if 'df' is a DataFrame and has required columns
    if not isinstance(df, pd.DataFrame) or not set(df.columns).issuperset({'date', 'value'}):
        raise ValueError("'df' is not a DataFrame or lacks required columns")

    # Create a cycle of colors for the groups
    colors = cycle(['blue', 'red', 'green', 'yellow', 'purple'])

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the scatter plot for each group
    for group, color in zip(groups, colors):
        ax.scatter(df[df['group'] == group]['date'], df[df['group'] == group]['value'], color=color)

    # Set the title, x-axis, and y-axis labels
    ax.set_title('Scatterplot of Values for Each Group Over Time')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')

    # Return the Axes object
    return ax