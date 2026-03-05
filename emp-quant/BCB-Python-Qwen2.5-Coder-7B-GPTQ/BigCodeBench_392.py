import numpy as np
import matplotlib.pyplot as plt
COLORS = ['r', 'g', 'b']
def task_func(df, group_col, value_col, group_name):
    """
    Create a bar subplot of a specific group from the input dataframe.
    
    Parameters:
    - df: pandas DataFrame containing the data.
    - group_col: The name of the column to group by.
    - value_col: The name of the column containing the values to plot.
    - group_name: The name of the group to plot.
    
    Returns:
    - Axes: A matplotlib axes object with the bar chart.
    
    Raises:
    - ValueError: If the group_name does not exist in df.
    """
    # Check if the group_name exists in the dataframe
    if group_name not in df[group_col].values:
        raise ValueError(f"The group_name '{group_name}' does not exist in the dataframe.")
    
    # Filter the dataframe for the specific group
    group_data = df[df[group_col] == group_name]
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(group_data[group_col], group_data[value_col], color=COLORS[0])
    
    # Set the title and labels
    ax.set_title(f'Bar chart of {value_col} for {group_name}')
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)
    
    return ax