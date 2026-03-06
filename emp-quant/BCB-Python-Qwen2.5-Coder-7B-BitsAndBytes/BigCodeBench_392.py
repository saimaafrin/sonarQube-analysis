
import numpy as np
import matplotlib.pyplot as plt

# Constants
COLORS = ['r', 'g', 'b']

def task_func(df, group_col, value_col, group_name):
    """
    Create a bar subplot of a specific group from the input dataframe.

    Parameters:
    - df (pd.DataFrame): Input dataframe containing the data.
    - group_col (str): Name of the column to group by.
    - value_col (str): Name of the column containing the values to plot.
    - group_name (str): The name of the group to create a bar chart for.

    Returns:
    - Axes: A matplotlib axes object with the bar chart.

    Raises:
    - ValueError: If the group_name does not exist in df.
    """
    # Check if the group_name exists in the dataframe
    if group_name not in df[group_col].values:
        raise ValueError(f"The group '{group_name}' does not exist in the dataframe.")

    # Filter the dataframe for the specific group
    group_data = df[df[group_col] == group_name][value_col]

    # Create a figure and an axes object
    fig, ax = plt.subplots()

    # Plot the bar chart
    bars = ax.bar(range(len(group_data)), group_data, color=COLORS[0])

    # Set the title and labels
    ax.set_title(f'Bar chart of {value_col} for {group_name}')
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)

    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

    return ax