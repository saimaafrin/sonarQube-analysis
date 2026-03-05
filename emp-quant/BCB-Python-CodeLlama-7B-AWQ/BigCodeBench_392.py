import numpy as np
import matplotlib.pyplot as plt
COLORS = ['r', 'g', 'b']
def task_func(df, group_col, value_col, group_name):
    """
    Create a bar subplot of a specific group from the input dataframe.
    """
    # Check if the group_name exists in the dataframe
    if group_name not in df[group_col].unique():
        raise ValueError(f"{group_name} does not exist in the dataframe")

    # Create a bar plot
    fig, ax = plt.subplots()
    ax.bar(df[group_col], df[value_col], color=COLORS[0])

    # Set the title and labels
    ax.set_title(f"Bar chart of {value_col} for {group_name}")
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)

    # Return the axes object
    return ax
df = pd.DataFrame({
    'group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'value': [1, 2, 3, 4, 5, 6]
})