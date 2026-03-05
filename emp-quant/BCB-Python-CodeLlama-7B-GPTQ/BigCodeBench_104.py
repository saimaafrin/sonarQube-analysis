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
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a DataFrame")

    # Check if df has required columns
    required_columns = ['Date', 'Value']
    if not all(column in df.columns for column in required_columns):
        raise ValueError("'df' must have columns 'Date' and 'Value'")

    # Create a cycle object to iterate over the groups
    group_cycle = cycle(groups)

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the scatter plot for each group
    for group in group_cycle:
        # Filter the data for the current group
        group_data = df[df['Group'] == group]

        # Plot the scatter plot
        ax.scatter(group_data['Date'], group_data['Value'], label=group)

    # Set the title, x-axis label, and y-axis label
    ax.set_title('Scatterplot of Values for Each Group Over Time')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')

    # Return the Axes object
    return ax
df = pd.DataFrame({
    'Date': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D']
})