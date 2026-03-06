
import pandas as pd
import matplotlib.pyplot as plt

def task_func(d, keys=['x', 'y', 'z']):
    # Create a Pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(d)

    # Plot the values of the specified keys
    ax = df[keys].plot(kind='line', figsize=(10, 6))

    # Return the Matplotlib Axes object
    return ax

ax = task_func(data, keys=['x', 'y'])

# Check the type of the returned object
print(type(ax))