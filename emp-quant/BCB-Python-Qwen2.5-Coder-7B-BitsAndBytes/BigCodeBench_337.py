
import numpy as np
import matplotlib.pyplot as plt

# Constants
COLORS = ['r', 'g', 'b']

def task_func(df, group_col, value_col):
    """
    Create a bar chart of data in multiple groups with error bars.

    Parameters:
    df (pd.DataFrame): DataFrame containing the data.
    group_col (str): Column name to group the data by.
    value_col (str): Column name containing the values to be plotted.

    Returns:
    Axes: A matplotlib axes object with the bar chart.
    """

    # Check if the value column contains only numeric values
    if not np.issubdtype(df[value_col].dtype, np.number):
        raise TypeError("The 'Value' column must contain only numeric values.")

    # Get unique groups
    groups = df[group_col].unique()
    
    # Number of groups
    n_groups = len(groups)
    
    # Calculate positions for each group
    index = np.arange(n_groups)
    bar_width = 0.35
    
    # Prepare data for plotting
    means = df.groupby(group_col)[value_col].mean().values
    stds = df.groupby(group_col)[value_col].std().values
    
    # Create figure and axis
    fig, ax = plt.subplots()

    # Plot bars
    for i, group in enumerate(groups):
        ax.bar(index + i * bar_width, means[i], bar_width,
               yerr=stds[i], capsize=5, color=COLORS[i % len(COLORS)],
               label=group)

    # Set labels and title
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)
    ax.set_title(f"Bar chart of {value_col} by {group_col}")
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(groups)
    ax.legend()

    return ax