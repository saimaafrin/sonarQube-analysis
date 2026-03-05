import numpy as np
import matplotlib.pyplot as plt
COLORS = ['r', 'g', 'b']
def task_func(df, group_col, value_col):
    """
    Create a bar chart of data in multiple groups with error bars.
    
    Parameters:
    - df: pandas DataFrame containing the data.
    - group_col: String, the name of the column to group by.
    - value_col: String, the name of the column containing the values to plot.
    
    Returns:
    - Axes: A matplotlib axes object with the bar chart.
    """
    # Check if value_col contains non-numeric values
    if not np.issubdtype(df[value_col].dtype, np.number):
        raise TypeError("The 'Value' column contains non-numeric values.")
    
    # Group data by group_col and calculate mean and standard deviation
    grouped_data = df.groupby(group_col)[value_col].agg(['mean', 'std']).reset_index()
    
    # Create bar chart
    fig, ax = plt.subplots()
    bars = ax.bar(grouped_data[group_col], grouped_data['mean'], yerr=grouped_data['std'], color=COLORS[:len(grouped_data)])
    
    # Set plot title and labels
    ax.set_title(f'Bar chart of {value_col} by {group_col}')
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)
    
    # Add color labels to each bar
    for bar, color in zip(bars, COLORS[:len(grouped_data)]):
        bar.set_color(color)
    
    return ax