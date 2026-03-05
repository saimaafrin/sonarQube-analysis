import pandas as pd
import matplotlib.pyplot as plt
def task_func(d, keys=['x', 'y', 'z']):
    """
    Plot values from a list of dictionaries based on specified keys and return the plot as a Matplotlib Axes object.
    """
    # Create a Pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(d)

    # Create a Matplotlib Axes object
    ax = df.plot(kind='line', x=keys[0], y=keys[1], z=keys[2])

    # Return the Matplotlib Axes object
    return ax
data = [
    {'x': 1, 'y': 2, 'z': 3},
    {'x': 4, 'y': 5, 'z': 6},
    {'x': 7, 'y': 8, 'z': 9},
]