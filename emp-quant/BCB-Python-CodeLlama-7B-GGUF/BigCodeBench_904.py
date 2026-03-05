
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data, keys=['x', 'y', 'z']):
    # Create a Pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(data)

    # Create a Matplotlib Axes object
    ax = plt.gca()

    # Plot the values of the specified keys
    for key in keys:
        ax.plot(df[key], label=key)

    # Set the title and labels
    ax.set_title('Plot of {}'.format(','.join(keys)))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    return ax