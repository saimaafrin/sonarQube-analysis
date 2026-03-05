import pandas as pd
import matplotlib.pyplot as plt
def task_func(d, keys=['x', 'y', 'z']):
    """
    Plot values from a list of dictionaries based on specified keys and return the plot as a Matplotlib Axes object.
    """
    # Convert the list of dictionaries to a Pandas DataFrame
    df = pd.DataFrame(d)

    # Create a new figure and axis object
    fig, ax = plt.subplots()

    # Plot the values of the specified keys on the axis
    for key in keys:
        ax.plot(df[key])

    # Return the axis object
    return ax
data = [
    {'x': 1, 'y': 2, 'z': 3},
    {'x': 4, 'y': 5, 'z': 6},
    {'x': 7, 'y': 8, 'z': 9},
]