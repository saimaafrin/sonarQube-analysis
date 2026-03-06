
import numpy as np
import matplotlib.pyplot as plt

# Constants
COLORS = ['r', 'g', 'b']

def task_func(df, group_col, value_col):
    # Check if the 'Value' column has non-numeric values
    if not all(df[value_col].apply(lambda x: isinstance(x, (int, float)))):
        raise TypeError("The 'Value' column has non-numeric values.")

    # Create a bar chart of the data
    fig, ax = plt.subplots()
    ax.bar(df[group_col], df[value_col], color=COLORS)

    # Add error bars
    ax.errorbar(df[group_col], df[value_col], yerr=df[value_col] / 2)

    # Set the plot title and labels
    ax.set_title(f"Bar chart of {value_col} by {group_col}")
    ax.set_xlabel(value_col)
    ax.set_ylabel(group_col)

    # Return the axes object
    return ax

ax = task_func(df, 'Group', 'Value')

# Show the plot
plt.show()