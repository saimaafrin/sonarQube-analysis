import pandas as pd
import matplotlib.pyplot as plt
def task_func(d, keys=['x', 'y', 'z']):
    """
    Plot values from a list of dictionaries based on specified keys and return the plot as a Matplotlib Axes object.
    """
    # Create a Pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(d)

    # Create a Matplotlib Axes object
    ax = plt.gca()

    # Plot the values of the specified keys
    for key in keys:
        ax.plot(df[key], label=key)

    # Set the title and labels
    ax.set_title('Plot of Values')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Return the Matplotlib Axes object
    return ax
data = [
    {'x': 1, 'y': 2, 'z': 3},
    {'x': 4, 'y': 5, 'z': 6},
    {'x': 7, 'y': 8, 'z': 9},
]