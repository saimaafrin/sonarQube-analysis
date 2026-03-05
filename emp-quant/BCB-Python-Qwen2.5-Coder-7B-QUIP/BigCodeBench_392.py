
import numpy as np
import matplotlib.pyplot as plt
# Constants
COLORS = ['r', 'g', 'b']

def task_func(df, group_col, value_col, group_name):
    """
    Create a bar subplot of a specific group from the input dataframe.
    
    Parameters:
    df (pd.DataFrame): The input dataframe.
    group_col (str): The name of the grouping column.
    value_col (str): The name of the value column.
    group_name (str): The name of the group to plot.
    
    Returns:
    Axes: A matplotlib axes object with the bar chart.
    
    Raises:
    ValueError: If the group_name does not exist in df.
    """
    # Check if the group_name exists in the dataframe
    if group_name not in df[group_col].unique():
        raise ValueError(f"Group name '{group_name}' does not exist in the dataframe.")
    
    # Filter the dataframe for the specific group
    group_df = df[df[group_col] == group_name]
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(group_df[group_col], group_df[value_col], color=COLORS[0])
    
    # Set the title and labels
    ax.set_title(f'Bar chart of {value_col} for {group_name}')
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)
    
    return ax