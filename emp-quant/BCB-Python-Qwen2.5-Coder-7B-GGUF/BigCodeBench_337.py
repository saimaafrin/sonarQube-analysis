
import numpy as np
import matplotlib.pyplot as plt
# Constants
COLORS = ['r', 'g', 'b']

def task_func(df, group_col, value_col):
    """
    Create a bar chart of data in multiple groups with error bars.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the data.
    group_col (str): Column name for the groups.
    value_col (str): Column name for the values.
    
    Returns:
    Axes: A matplotlib axes object with the bar chart.
    
    Raises:
    TypeError: If the 'Value' has non-numeric values.
    """
    # Check if the value column contains non-numeric values
    if not np.issubdtype(df[value_col].dtype, np.number):
        raise TypeError("The 'Value' column contains non-numeric values.")
    
    # Group the data by the group column
    grouped = df.groupby(group_col)
    
    # Prepare data for plotting
    labels = grouped.groups.keys()
    values = [group[value_col].mean() for _, group in grouped]
    errors = [group[value_col].std() for _, group in grouped]
    
    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(labels, values, yerr=errors, color=[COLORS[i % len(COLORS)] for i in range(len(labels))])
    
    # Set the title and labels
    ax.set_title(f'Bar chart of {value_col} by {group_col}')
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)
    
    return ax