import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle
def task_func(df, groups=['A', 'B', 'C', 'D', 'E']):
    """
    Analyzes the groups in a DataFrame by plotting a scatter plot of the ordinals against the values for each group.
    The function should raise the exception for: ValueError: If 'df' is not a DataFrame or lacks required columns.
    The function should output with:
        matplotlib.axes.Axes: The Axes object with the scatter plot.
        The Axes object will have a title 'Scatterplot of Values for Each Group Over Time',
        x-axis labeled as 'Date (ordinal)', and y-axis labeled as 'Value'.
    """
    # Check if 'df' is a DataFrame and lacks required columns
    if not isinstance(df, pd.DataFrame) or not set(df.columns).issuperset({'Date', 'Value'}):
        raise ValueError("'df' is not a DataFrame or lacks required columns")

    # Create a list of colors for each group
    colors = cycle(['red', 'blue', 'green', 'yellow', 'orange'])

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the scatter plot for each group
    for group in groups:
        # Select the data for the current group
        group_data = df[df['Group'] == group]

        # Plot the scatter plot
        ax.scatter(group_data['Date'], group_data['Value'], c=next(colors))

    # Set the title, x-axis label, and y-axis label
    ax.set_title('Scatterplot of Values for Each Group Over Time')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')

    # Return the Axes object
    return ax
df = pd.DataFrame({'Date': [1, 2, 3, 4, 5], 'Value': [10, 20, 30, 40, 50], 'Group': ['A', 'A', 'B', 'B', 'C']})