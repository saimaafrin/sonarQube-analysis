
import numpy as np
import matplotlib.pyplot as plt
# Constants
COLORS = ['r', 'g', 'b']

def task_func(df, group_col, value_col):
    """
    Create a bar chart of data in multiple groups with error bars.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    group_col (str): The column name for the groups.
    value_col (str): The column name for the values.
    
    Returns:
    matplotlib.axes.Axes: A matplotlib axes object with the bar chart.
    
    Raises:
    TypeError: If the 'Value' has non-numeric values.
    """
    # Check if the value column contains only numeric values
    if not df[value_col].dtype.kind in "fi":
        raise TypeError("The 'Value' column must contain only numeric values.")
    
    # Get unique groups
    groups = df[group_col].unique()
    
    # Get the number of groups
    num_groups = len(groups)
    
    # Get the number of bars
    num_bars = len(df[value_col])
    
    # Get the width of each bar
    width = 0.8
    
    # Get the index for each group
    index = np.arange(num_bars)
    
    # Get the error values (assuming they are in a column named 'error')
    error = df['error'].values
    
    # Create the bar chart
    fig, ax = plt.subplots()
    for i, group in enumerate(groups):
        ax.bar(index + i * width, df[value_col].values, width, color=COLORS[i % len(COLORS)], label=group)
    
    # Add error bars
    ax.errorbar(x=index, y=df[value_col].values, yerr=error, fmt='o', ecolor='black', capsize=5)
    
    # Set the title and labels
    ax.set_title(f"Bar chart of {value_col} by {group_col}")
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)
    
    # Set the tick labels
    ax.set_xticks(index + width / 2)
    ax.set_xticklabels(df[group_col].unique())
    
    # Show the legend
    ax.legend()
    
    return ax