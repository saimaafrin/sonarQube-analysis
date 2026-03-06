from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
def task_func(list_of_menuitems):
    """
    Given a nested list of menu items, this function flattens the list and visualizes the frequency
    of each menu item using a seaborn barplot.

    Parameters:
        list_of_menuitems (list): A nested list of menu items.

    Returns:
        matplotlib.axes.Axes: An Axes object representing the visualization, or None if there are no items to plot.

    Requirements:
        - collections
        - seaborn
        - pandas
        - matplotlib

    Example:
        >>> ax = task_func([['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']])
        >>> isinstance(ax, matplotlib.axes.Axes)
        True
    """
    # Flatten the list
    flat_list = [item for sublist in list_of_menuitems for item in sublist]

    # Count the frequency of each item
    counter = Counter(flat_list)

    # Create a dataframe from the counter
    df = pd.DataFrame.from_dict(counter, orient='index')

    # Plot the dataframe
    ax = sns.barplot(x=df.index, y=df.values)

    return ax