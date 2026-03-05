
import numpy as np
import matplotlib.pyplot as plt
# Constants
COLORS = ['r', 'g', 'b']
def task_func(df, group_col, value_col):
    # Check if the 'Value' column has non-numeric values
    if not np.issubdtype(df[value_col].dtype, np.number):
        raise TypeError("'Value' column has non-numeric values")
    
    # Create a bar chart of the data
    fig, ax = plt.subplots()
    ax.bar(df[group_col], df[value_col], color=COLORS)
    ax.set_title(f"Bar chart of {value_col} by {group_col}")
    ax.set_xlabel(value_col)
    ax.set_ylabel(group_col)
    ax.errorbar(df[group_col], df[value_col], yerr=df[value_col] / 2)
    return ax