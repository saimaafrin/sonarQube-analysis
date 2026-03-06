
import pandas as pd
import matplotlib.pyplot as plt

def task_func(d, keys=['x', 'y', 'z']):
    """
    Plots values from a list of dictionaries based on specified keys and returns the plot as a Matplotlib Axes object.

    Parameters:
    d (list of dict): List of dictionaries containing data.
    keys (list of str): Keys to be plotted. Default is ['x', 'y', 'z'].

    Returns:
    matplotlib.axes._axes.Axes: The plot showing the values of specified keys from the input list of dictionaries.
    """
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(d)
    
    # Plot the specified keys
    ax = df[keys].plot(kind='line')
    
    # Set labels and title
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    ax.set_title('Plot of Specified Keys')
    
    return ax

ax = task_func(data, keys=['x', 'y'])
print(type(ax))  # Should print: <class 'matplotlib.axes._subplots.AxesSubplot'>

# Display the plot
plt.show()