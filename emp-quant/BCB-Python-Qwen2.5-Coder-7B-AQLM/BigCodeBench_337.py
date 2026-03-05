
import numpy as np
import matplotlib.pyplot as plt

# Constants
COLORS = ['r', 'g', 'b']

def task_func(df, group_col, value_col):
    """
    Create a bar chart of data in multiple groups with error bars.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame containing the data.
    group_col (str): The column name for the groups.
    value_col (str): The column name for the values.
    
    Returns:
    Axes: A matplotlib axes object with the bar chart.
    
    Raises:
    TypeError: If the 'Value' has non-numeric values.
    """
    # Check if the value column contains non-numeric values
    if not np.issubdtype(df[value_col].dtype, np.number):
        raise TypeError("The 'Value' column contains non-numeric values.")
    
    # Get unique groups and sort them
    groups = sorted(df[group_col].unique())
    
    # Calculate means and standard deviations for each group
    means = df.groupby(group_col)[value_col].mean()
    std_devs = df.groupby(group_col)[value_col].std()
    
    # Create a bar chart
    fig, ax = plt.subplots()
    bar_width = 0.35
    index = np.arange(len(groups))
    
    for i, group in enumerate(groups):
        ax.bar(index + i * bar_width, means[group], bar_width, yerr=std_devs[group], color=COLORS[i % len(COLORS)], label=group)
    
    # Set labels and title
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)
    ax.set_title(f"Bar chart of {value_col} by {group_col}")
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(groups)
    ax.legend()
    
    return ax