import numpy as np
import matplotlib.pyplot as plt
COLORS = ['r', 'g', 'b']
def task_func(df, group_col, value_col):
    """
    Create a bar chart of data in multiple groups with error bars.
    
    Parameters:
    - df: pandas DataFrame containing the data.
    - group_col: The column name to group by.
    - value_col: The column name containing the values to plot.
    
    Returns:
    - Axes: A matplotlib axes object with the bar chart.
    """
    # Check if the value column contains non-numeric values
    if not np.issubdtype(df[value_col].dtype, np.number):
        raise TypeError("The 'Value' column contains non-numeric values.")
    
    # Group data by the group column
    grouped_data = df.groupby(group_col)[value_col].agg(['mean', 'std'])
    
    # Get unique groups and their corresponding colors
    groups = grouped_data.index
    colors = [COLORS[i % len(COLORS)] for i in range(len(groups))]
    
    # Create the bar chart
    fig, ax = plt.subplots()
    bars = ax.bar(groups, grouped_data['mean'], yerr=grouped_data['std'], color=colors)
    
    # Set plot title and labels
    ax.set_title(f'Bar chart of {value_col} by {group_col}')
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)
    
    return ax