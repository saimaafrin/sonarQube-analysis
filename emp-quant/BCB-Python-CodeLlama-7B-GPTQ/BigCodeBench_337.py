import numpy as np
import matplotlib.pyplot as plt
COLORS = ['r', 'g', 'b']
def task_func(df, group_col, value_col):
    """
    Create a bar chart of data in multiple groups with error bars.
    """
    # Check if the 'Value' column has non-numeric values
    if not all(df[value_col].apply(lambda x: isinstance(x, (int, float)))):
        raise TypeError("The 'Value' column must contain only numeric values.")
    # Create a new figure and axis object
    fig, ax = plt.subplots()
    # Set the title of the plot
    ax.set_title(f"Bar chart of {value_col} by {group_col}")
    # Set the x-axis label
    ax.set_xlabel(value_col)
    # Set the y-axis label
    ax.set_ylabel(group_col)
    # Create a bar plot
    ax.bar(df[group_col], df[value_col], yerr=df[value_col], color=COLORS)
    # Set the error bar color
    ax.errorbar(df[group_col], df[value_col], yerr=df[value_col], color=COLORS)
    # Return the axis object
    return ax
df = pd.DataFrame({
    "Group": ["A", "B", "C", "A", "B", "C"],
    "Value": [10, 20, 30, 15, 25, 35],
    "Error": [2, 4, 6, 3, 5, 7]
})