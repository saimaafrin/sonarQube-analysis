from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
def task_func(list_of_menuitems):
    """
    Given a nested list of menu items, this function flattens the list and visualizes the frequency of each menu item using a seaborn barplot.
    The function should output with:
        matplotlib.axes.Axes: An Axes object representing the visualization, or None if there are no items to plot.
    """
    # Flatten the list of menu items
    flat_list = [item for sublist in list_of_menuitems for item in sublist]

    # Create a Counter object to count the frequency of each menu item
    counter = Counter(flat_list)

    # Create a Pandas DataFrame from the Counter object
    df = pd.DataFrame.from_dict(counter, orient='index')

    # Sort the DataFrame by the frequency of each menu item
    df.sort_values(by='count', inplace=True)

    # Create a Seaborn barplot from the DataFrame
    ax = sns.barplot(x='index', y='count', data=df)

    # Return the Axes object representing the visualization
    return ax